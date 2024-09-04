# Hale Center Repository

The Hale Center repository is a resource for data download and exploration of samples generated by Dr. Stephanie Dougan's Lab at the Hale center. The website is accessible at this URL ONLY within the DFCI network or while connected over VPN: http://haledatarepo.dfci.harvard.edu/. 

### Code Organization

The website components are integrated using Flask, which is a Python web framework. Some of these components are written in R (i.e. Data Exploration) and some are written in Dash (i.e. Clinical Data and Data Download). The format of the website repository follows the "Flask Application Factory" pattern which is nicely explained here: https://hackersandslackers.com/flask-application-factory/. Briefly, the structure of the repository is as follows:

  ##### hale-center-repository:
        #### activate_venv.sh => a Bash script that is called upon deployment, that activates the Python virtual environment with all the packages required for the website to run.
        #### wsgi.py => creates the Flask app object by calling the "init_app()" function from "hale_center_repository/__init__.py". 
  ##### hale_center_repository:
      This directory follows the structure of pretty much any typical Flask app, where the Dash files and HTML files are stored separately in subfolders. The structure is briefly described below:
        #### templates => a directory with html files for each subpage. "base.html" defines the basic structure/elements of the website like the menu, and header so that we don't have to re-type all of that every time we create a new subpage. Each subpage inherits this base.html template so that the website is uniform. 
        #### static => holds static files like the logo.png and other images used throughout the website. 
        #### plotlydash => a directory with python files that hold the code for the data download and data exploration components of the website. 
        #### data => holds the data used the website like the excel tables and the count matrices for download (this data is only on the server and not pushed to this repo). 

The website has 4 subpages or tabs: Home, Clinical Data, Data Exploration, and Data Download. 
