import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
    html.Label('Slider'),
    dcc.Slider(
        min=-10,
        max=10,
        step=0.5,
        marks={i: i for i in range(-10, 10)},
        value=0
    ),
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),
    html.Label('Text Input'),
    dcc.Input(
        value='MTL',
        type='text'
    ),
    html.Label('Text Area'),
    dcc.Textarea(
        value='MTL',
        style={
            'width': '100%'
        }
    ),
    html.Label('Markdown'),
    dcc.Markdown('''
        Dash and Markdown
        
        Dash supports [Markdown](http://commonmark.org/help).
        
        Markdown is a simple way to write and format text.
        It includes a syntax for things like **bold text** and *italics*,
        [links](http://commonmark.org/help), inline `code` snippets, lists,
        quotes, and more.
    '''),
    html.Label('Graph'),
    dcc.Graph(
        figure={
            'data': [
{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server()