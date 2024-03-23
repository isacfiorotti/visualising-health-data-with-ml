import dash
import dash_html_components as html
import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

import render as rd

#---------------------------------------------------------------------------------#

# Testing parameters

# Features to be displayed
x_feat = "Time(s)"
y_feat = "Arterial pressure (mmHg)"

path = "/Users/isacfiorotti/Library/CloudStorage/OneDrive-TheUniversityofNottingham/Modules/COMP4031 - Personal Project/data/data.csv"
header_names = ['Time(s)', 'Arterial pressure (mmHg)', 'Aortic Doppler (kHz)',
       'Mesenteric Doppler (kHz)', 'Renal Doppler (kHz)']

width = 1000
height = 400

#---------------------------------------------------------------------------------#``

def main():

    # Read data
    ddf = rd.read_csv(path, header_names)
    rd.plot_raster(ddf, width, height, x_feat, y_feat)

    run_simple('localhost', 8050, server)

    return None

#---------------------------------------------------------------------------------#

# Create a Flask app that serves the Dash app which is created from main.py
server = flask.Flask(__name__)

@server.route('/')
def index():
    return 'Hello, World!'

#---------------------------------------------------------------------------------#
    
if __name__ == "__main__":
    main()
