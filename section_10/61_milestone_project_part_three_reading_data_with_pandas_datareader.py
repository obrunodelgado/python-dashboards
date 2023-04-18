import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
from datetime import datetime

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol:'),
    dcc.Input(id='my_stock_picker', value='MSFT'),
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


@app.callback(
    Output('my_graph', 'figure'),
    [Input('my_stock_picker', 'value')]
)
def update_graph(stock_ticker):
    start = datetime(2022, 1, 1)
    end = datetime(2022, 12, 31)
    df = web.DataReader(stock_ticker, 'stooq', start, end)

    fig = {
        'data': [
            {'x': df.index, 'y': df['Close']}
        ],
        'layout': {'title': stock_ticker}
    }
    return fig


if __name__ == '__main__':
    app.run_server()
