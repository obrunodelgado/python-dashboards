import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(
    [
        html.H1(id='live-update-text'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ]
)


@app.callback(
    Output('live-update-text', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_layout(n):
    return f'Number of intervals: {n}'


if __name__ == '__main__':
    app.run_server()