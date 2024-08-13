"""Instantiate a Dash app."""
import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load data
df = pd.read_excel("/var/www/hale-center-repository/hale_center_repository/data/ClinicalData_PRAIII.xlsx")
options = {col: col.lower().replace(" ", "-") for col in df.columns}

# Define column definitions for AG Grid
column_defs = [{"field": "", "checkboxSelection": False, "headerCheckboxSelection": False, "width": 45, "pinned": "left", "filterParams": {"readOnly": True}}]

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

def init_data_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dash_clinical_data/',
    )


    dash_app.layout = html.Div([
        html.Div(className='content', children=[
            html.Div(),
            dbc.Row([
                dbc.Col([
                    dag.AgGrid(
                        rowData=df.to_dict('records'),
                        style={"padding": '15px 50px 5px 50px', "height": 800, "width": 1700},
                        columnDefs=column_defs,
                        defaultColDef={'filter': True},
                        id='grid'
                    )
                ], width='3')
            ]),
        ]),
        html.P([
            "Pathological Response Score:",
            html.Br(),
            "0 = pCR (pathologic complete response)",
            html.Br(),
            "1 = single cells or rare small groups of cancer cells",
            html.Br(),
            "2 = Residual cancer with evident tumor regression, but more than single cells or rare small groups of cancer cells",
            html.Br(),
            "3 = No pathologic response",
        ],
        style = {'font-family': 'Arial, sans-serif'}),
    ])
    return dash_app.server

