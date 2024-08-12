"""Routes for parent Flask app."""
from flask import render_template
from flask import current_app as app


@app.route('/')
def home():
    """Landing page."""
    return render_template(
        'home.html',
        title='Plotly Dash Flask Tutorial',
        description='Embed Plotly Dash into your Flask applications.',
        template='home-template',
        body="This is a homepage served with Flask."
    )

@app.route('/clinical-data')
def clinical_data():
    return render_template("clinical-data.html", dash_url = "/dash_clinical_data" )

@app.route('/data-download')
def data_download():
    return render_template("data-download.html", dash_url = "/dash_data_download")

@app.route('/explore-data')
def explore_data():
    return render_template("explore-data.html")

