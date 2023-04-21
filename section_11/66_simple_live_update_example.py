import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import requests

counter_list = []

app = dash.Dash()

app.layout = html.Div(
    [
        html.Div(
            [
                html.Pre(id='counter-text', children='Active flights worldwide:'),
                dcc.Graph(id='live-update-graph', style={'width': '100%'}),
                dcc.Interval(
                    id='interval-component',
                    interval=6000, # in milliseconds
                    n_intervals=0
                )
            ]
        )
    ]
)


@app.callback(
    Output('counter-text', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_layout(n):
    url = 'https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1&mlat=1&flarm=1&adsb=1&air=1&vehicles=1' \
          '&estimated=1&gliders=1&stats=1'
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = response.json()
    counter = 0

    for element in data['stats']['total']:
        counter += data['stats']['total'][element]

    counter_list.append(counter)

    return f'Active flights worldwide: {counter}'


@app.callback(
    Output('live-update-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    fig = go.Figure(
        data=[
            go.Scatter(
                x=list(range(len(counter_list))),
                y=counter_list,
                mode='lines+markers'
            )
        ],
    )

    return fig


if __name__ == '__main__':
    app.run_server()
