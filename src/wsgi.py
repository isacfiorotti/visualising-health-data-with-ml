from app import init_app
from flaskwebgui import FlaskUI

app = init_app()

if __name__ == "__main__":
    ui = FlaskUI(app=app, server="flask").run()