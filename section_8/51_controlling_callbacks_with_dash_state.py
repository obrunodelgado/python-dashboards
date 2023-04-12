import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Input(
            id='number-in',
            value=1,
            style={'fontSize': 28}
        ),
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontSize': 28}
        ),
        html.H1(id='number-out')
    ]
)


@app.callback(
    Output('number-out', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('number-in', 'value')]
)
def on_change_a(n_clicks, value):
    return f"{value} was submitted {n_clicks} times"


if __name__ == '__main__':
    app.run_server()