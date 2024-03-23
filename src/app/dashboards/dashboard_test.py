import dash
from dash import dcc, html
import plotly.graph_objs as go

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )

    dash_app.layout = html.Div([
        html.H1('My Dash Application'),
        dcc.Graph(
            id='dash-container',
            figure={
                'data': [
                    go.Scatter(
                        x=[1, 2, 3, 4],
                        y=[10, 15, 13, 17],
                        mode='lines+markers',
                        name='Line chart'
                    )
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ])

    return dash_app.server