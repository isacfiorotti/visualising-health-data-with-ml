import dash
from dash import dcc, html
import plotly.graph_objs as go
import plotly.express as px

# Builder for treemap 

def build_graph():

    fig = px.treemap(
        names = ["1","2", "3", "4", "5", "6", "7", "8", "9"],
        parents = ["", "1", "1", "2", "2", "3", "3", "4", "4"],
    )
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

    # returning the figure
    return fig

def init_tree_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashtree/'
    )

    dash_app.layout = html.Div(
        dcc.Graph(
            id='dash-container',
            figure=build_graph()
        )
    )

    return dash_app.server
