from flask import Flask
from .dashboards.dashboard_test import init_dashboard

# Flask app

def init_app():
    app = Flask(__name__)
    
    with app.app_context():
        from . import routes
        app = init_dashboard(app)

    return app

