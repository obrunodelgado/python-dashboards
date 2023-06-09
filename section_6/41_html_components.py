import dash
from dash import html

app = dash.Dash()

app.layout = html.Div(
    [
        'This is the outermost div!',
        html.Div(
            'This is an inner div!',
            style={
                'color': 'red',
                'border': '2px red solid'
            }
        ),
        html.Div(
            'This is another inner div!',
            style={
                'color': 'green',
                'border': '2px green solid'
            }
        )
    ],
    style={
      'color': 'blue',
      'border': '2px blue solid'
    }
)

if __name__ == '__main__':
    app.run_server()