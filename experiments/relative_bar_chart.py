import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/My_2018WinterOlympics.csv')

data = go.Bar(
    x=df['Total'],
    y=df['NOC'],
    orientation='h',
    name='Call',
    marker=dict(
        color=df['Total'],
        colorscale='Ice',
        reversescale=True
    )
)

data2 = go.Bar(
    x=df['Test'],
    y=df['NOC'],
    orientation='h',
    name='Put',
    marker=dict(
        color=df['Test'],
        colorscale='Reds',
        reversescale=True
    )
)

layout = go.Layout(
    title='2018 Winter Olympics Medals by Country',
    barmode='relative',
    plot_bgcolor='#000'
)

fig = go.Figure(data=[data, data2], layout=layout)

pyo.plot(fig, filename='../charts/relative_bar_chart.html')