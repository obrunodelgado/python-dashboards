import random

import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')
df['year'] = random.randint(-4, 5, len(df)) * 0.1 + df['model_year']

app.layout = html.Div(
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
            }),
    ]
)

if __name__ == '__main__':
    app.run_server()
