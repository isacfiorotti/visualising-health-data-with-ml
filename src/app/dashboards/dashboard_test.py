import dash
from dash import dcc, html
import plotly.graph_objs as go
from app import render as rd
import plotly.express as px

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

#---------------------------------------------------------------------------------#

def build_graph():
    ddf = rd.read_csv(path, header_names)
    img = rd.rasterise(ddf.compute(), width, height, x_feat, y_feat)
    fig = px.imshow(img)
    return fig


def init_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )

    dash_app.layout = html.Div([
        html.H1('My Dash Application'),
        dcc.Graph(
            id='dash-container',
            figure=build_graph()
        )
    ])

    return dash_app.server