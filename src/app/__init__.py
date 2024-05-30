from flask import Flask
from .dashboards.timeseries import init_timeseries_dashboard
from .dashboards.treemap import init_tree_dashboard

# Flask app

def init_app():
    app = Flask(__name__)
    
    with app.app_context():
        from . import routes
        app = init_timeseries_dashboard(app)
        app = init_tree_dashboard(app)

    return app

