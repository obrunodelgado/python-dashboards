import base64

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()

df = pd.read_csv('../data/wheels.csv')

app.layout = html.Div(
    [
        html.Div(
            dcc.Graph(
                id='wheels-plot',
                figure={
                    'data':
                        [
                            go.Scatter(
                                x=df['color'],
                                y=df['wheels'],
                                dy=1,
                                mode='markers',
                                marker={'size': 15}
                            )
                        ],
                    'layout': go.Layout(
                        title='Test',
                        xaxis={'title': 'Color'},
                        yaxis={'title': 'Wheels'},
                        hovermode='closest'
                    )
                }
            ),
            style={
                'width': '30%',
                'float': 'left'
            }
        ),
        html.Div(
            html.Img(
                id='hover-data',
                src='children',
                height=300
            ),
            style={'paddingTop': 35}
        ),
    ]
)


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return f'data:image/png;base64,{encoded.decode()}'

@app.callback(
    Output('hover-data', 'src'),
    [Input('wheels-plot', 'hoverData')]
)
def callback_image(hoverData):
    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path = '../data/images/'

    return encode_image(path + df[(df['wheels'] == wheel) & (df['color'] == color)]['image'].values[0])


if __name__ == '__main__':
    app.run_server()