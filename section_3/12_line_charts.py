import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

markers = go.Scatter(
    x=x_values,
    y=y_values+5,
    mode='markers',
    name='markers'
)

lines = go.Scatter(
    x=x_values,
    y=y_values,
    mode='lines',
    name='mylines'
)

linesAndMarkers = go.Scatter(
    x=x_values,
    y=y_values-5,
    mode='lines+markers',
    name='myfavorite'
)

data = [markers, lines, linesAndMarkers]

layout = go.Layout(
    title='Line Charts'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='../charts/line.html')