from app import init_app
from flaskwebgui import FlaskUI

app = init_app()

if __name__ == "__main__":

    # Deploys the python app as a desktop application using flaskwebgui
    FlaskUI(app=app, server="flask").run()
