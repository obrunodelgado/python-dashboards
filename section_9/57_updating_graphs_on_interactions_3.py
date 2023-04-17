import random

import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
from numpy import random
from dash.dependencies import Input, Output

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')
df['year'] = random.randint(-4, 5, len(df)) * 0.1 + df['model_year']

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id='mpg-scatter',
                    figure={
                        'data': [
                            go.Scatter(
                                x=df['year'] + 1900,
                                y=df['mpg'],
                                text=df['name'],
                                hoverinfo='text+y+x',
                                mode='markers',
                            )
                        ],
                        'layout': go.Layout(
                            title='Acceleration vs. Displacement',
                            xaxis={'title': 'Model Year'},
                            yaxis={'title': 'MPG'},
                            hovermode='closest'
                        )
                    }
                )
            ],
            style={
                'width': '50%',
                'display': 'inline-block'
            }
        ),
        html.Div(
            [
                dcc.Graph(
                    id='mpg-line',
                    figure={
                        'data': [
                            go.Scatter(
                                x=[0, 1],
                                y=[0, 1],
                                mode='lines'
                            )
                        ],
                        'layout': go.Layout(
                            title='Acceleration',
                            margin={'l': 0}
                        )
                    }
                )
            ],
            style={
                'width': '20%',
                'height': '50%',
                'display': 'inline-block'
            }
        ),
        html.Div(
            [
                dcc.Markdown(id='mpg-stats')
            ],
            style={
                'width': '20%',
                'height': '50%',
                'display': 'inline-block'
            }
        )
    ]
)


@app.callback(
    Output('mpg-line', 'figure'),
    [
        Input('mpg-scatter', 'hoverData')
    ]
)
def callback_graph(hoverData):
    if hoverData is None:
        return {
            'data': [
                go.Scatter(
                    x=[0, 1],
                    y=[0, 1],
                    mode='lines'
                )
            ],
            'layout': go.Layout(
                title='Acceleration',
                margin={'l': 0}
            )
        }

    v_index = hoverData['points'][0]['pointIndex']
    figure = {
        'data': [
            go.Scatter(
                x=[0, 1],
                y=[0, 60 / df.iloc[v_index]['acceleration']],
                mode='lines',
                line={'width': 2 * df.iloc[v_index]['cylinders']}
            )
        ],
        'layout': go.Layout(
            title='Acceleration',
            margin={'l': 0},
            xaxis={'visible': False},
            yaxis={'visible': False, 'range': [0, 60 / df['acceleration'].min()]},
            height=300
        )
    }
    return figure


@app.callback(
    Output('mpg-stats', 'children'),
    [
        Input('mpg-scatter', 'hoverData')
    ]
)
def callback_stats(hoverData):
    if hoverData is None:
        return 'Hover over a point to see its acceleration'

    v_index = hoverData['points'][0]['pointIndex']
    stats = """
        {} cylinders
        {} cc displacement
        0 to 60mph in {} seconds
    """.format(
        df.iloc[v_index]['cylinders'],
        df.iloc[v_index]['displacement'],
        df.iloc[v_index]['acceleration']
    )
    return stats


if __name__ == '__main__':
    app.run_server()
