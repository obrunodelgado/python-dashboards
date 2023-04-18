import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol:'),
    dcc.Input(id='my_stock_picker', value='TSLA'),
    dcc.Graph(
        id='my_graph',
        figure={
            'data':
                [
                    {'x': [1, 2], 'y': [3, 1]}
                ],
            'layout': {'title': 'Default Title'}
        }
    )
])


if __name__ == '__main__':
    app.run_server()
