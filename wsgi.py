from hale_center_repository import init_app

dashboard_app, download_app = init_app()

if __name__ == "__main__":
    dashboard_app.run(host='0.0.0.0')
    download_app.run(host='0.0.0.0')
