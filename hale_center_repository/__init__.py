from flask import Flask

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes

        from .plotlydash.clinical_data import init_data_dashboard
        dashboard_app = init_data_dashboard(app)
        from .plotlydash.data_download import init_data_download
        download_app = init_data_download(app)

        return dashboard_app, download_app
