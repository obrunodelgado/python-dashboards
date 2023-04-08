import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1('Dash Tutorials'),
    ]
)

if __name__ == '__main__':
    app.run_server()