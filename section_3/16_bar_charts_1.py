import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/2018WinterOlympics.csv')

data = [go.Bar(
    x=df['NOC'],
    y=df['Total']
)]

layout = go.Layout(
    title='2018 Winter Olympics Medals by Country'
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='../charts/16_bar_charts.html')