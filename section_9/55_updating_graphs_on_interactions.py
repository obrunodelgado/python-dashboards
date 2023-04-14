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
        dcc.Graph(id='mpg-scatter',
                  figure={
                      'data': [
                          go.Scatter(
                              x=df['year'] + 1900,
                              y=df['mpg'],
                              text=df['name'],
                              hoverinfo='text+y+x',
                              mode='markers',
                              # marker={
                              #     'size': 15,
                              #     'opacity': 0.5,
                              #     'line': {'width': 0.5, 'color': 'white'}
                              # }
                          )
                      ],
                      'layout': go.Layout(
                          title='Acceleration vs. Displacement',
                          xaxis={'title': 'Model Year'},
                          yaxis={'title': 'MPG'},
                          hovermode='closest'
                      )
                  }),
        # html.Div([
        #     dcc.Graph(id='mpg-line', figure={
        #         'data': [
        #             go.Scatter(
        #                 x=[0, 1],
        #                 y=[0, 1],
        #                 mode='lines'
        #             )
        #         ]
        #     })
        # ], style={'width': '30%', 'display': 'inline-block'})
    ]
)

if __name__ == '__main__':
    app.run_server()
