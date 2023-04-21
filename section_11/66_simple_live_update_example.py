import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import requests

app = dash.Dash()

app.layout = html.Div(
    [
        html.Div(
            [
                html.Pre(id='counter-text', children='Active flights worldwide:'),
                dcc.Interval(
                    id='interval-component',
                    interval=6*1000, # in milliseconds
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

    return f'Active flights worldwide: {counter}'


if __name__ == '__main__':
    app.run_server()
