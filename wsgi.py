import sys
import subprocess

sys.path.append("/var/www/hale-center-repository")
sys.path.append("/var/www/hale-center-repository/hale_center_repository")
from hale_center_repository import init_app

env_name = "hale-center"
subprocess.run(["bash", "/var/www/hale-center-repository/activate_venv.sh"])

application, download_app = init_app()

if __name__ == "__main__":
    application.run(host='0.0.0.0')
    download_app.run(host='0.0.0.0')
