"""Instantiate a Dash app."""
import dash
from dash import dash_table, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd

from flask import send_file
import os
import zipfile
import tempfile

BASE_DIR = "/Volumes/sdougan/PDAC_Data_Repository/cellranger_processed_data"

# Load data
df = pd.read_excel("hale_center_repository/data/PRAIII_Data_Download.xlsx")
options = {col: col.lower().replace(" ", "-") for col in df.columns}

# Define column definitions for AG Grid
column_defs = [{"field": "", "checkboxSelection": True, "headerCheckboxSelection": True, "width": 45, "pinned": "left", "filterParams": {"readOnly": True}}]
column_defs.extend([
    {
        "field": i,
        "columnSize": "autoSize",
        "filterParams": {
            "readOnly": True,
            "maxNumConditions": len(df[i].unique())
        }
    } for i in df.columns
])

def init_data_download(server):
    dash_app = dash.Dash(
        server=server,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        routes_pathname_prefix='/dash_data_download/',
    )

    dash_app.layout = html.Div([
        html.Div(className='content', children=[
            html.Button("Download Selected Datasets", id="download-button", n_clicks=0),
            dcc.Download(id="download-zip"),
            html.Div(),
            dbc.Row([
                dbc.Col([
                    dag.AgGrid(
                        rowData=df.to_dict('records'),
                        style={"padding": '15px 50px 5px 50px', "height": 800, "width": 1700},
                        dashGridOptions={"rowSelection": "multiple", "animateRows": False},
                        columnDefs=column_defs,
                        defaultColDef={'filter': True},
                        id='grid'
                    )
                ], width='3')
            ]),
        ])
    ])
    init_callbacks(dash_app)
    return dash_app.server

def init_callbacks(dash_app):
    @dash_app.callback(
        Output("download-zip", "data"),
        Input("download-button", "n_clicks"),
        State("grid", "selectedRows"),
        prevent_initial_call = True
    )
    def download_selected_datasets(n_clicks, selected_rows):
        # Get the selected dataset IDs
        selected_dataset_ids = set([r["Dataset ID"] for r in selected_rows])

        # Create a temporary directory to store the files to be zipped
        with tempfile.TemporaryDirectory() as tmpdirname:
            zip_path = os.path.join(tmpdirname, 'pdac_data_repository.zip')

            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for dataset_id in selected_dataset_ids:
                    dataset_dir = os.path.join(BASE_DIR, dataset_id)
                    dataset_dir = dataset_dir.replace(" ", "")
                    print(os.path.exists(dataset_dir))
                    print(dataset_dir.split(" "))
                    if os.path.exists(dataset_dir):
                        for root, dirs, files in os.walk(dataset_dir):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, BASE_DIR)
                                zipf.write(file_path, arcname)

            # Return the zip file for download
            return dcc.send_file(zip_path, filename="pdac_data_repository.zip")

