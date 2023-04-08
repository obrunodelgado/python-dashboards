import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import subplots
import pandas as pd

df = pd.read_csv('../data/2010SitkaAK.csv')
df2 = pd.read_csv('../data/2010SantaBarbaraCA.csv')
df3 = pd.read_csv('../data/2010YumaAZ.csv')

trace1 = go.Heatmap(
    x=df['DAY'],
    y=df['LST_TIME'],
    z=df['T_HR_AVG'].values.tolist(),
    colorscale='Jet',
    name='Sitka',
    zmin=5,
    zmax=40
)

trace2 = go.Heatmap(
    x=df2['DAY'],
    y=df2['LST_TIME'],
    z=df2['T_HR_AVG'].values.tolist(),
    colorscale='Jet',
    name='SB CA',
    zmin=5,
    zmax=40
)

trace3 = go.Heatmap(
    x=df3['DAY'],
    y=df3['LST_TIME'],
    z=df3['T_HR_AVG'].values.tolist(),
    colorscale='Jet',
    name='Yuma AZ',
    zmin=5,
    zmax=40
)

fig = subplots.make_subplots(rows=1, cols=3, subplot_titles=['Sitka AK', 'SB CA', 'Yuma AZ'], shared_yaxes=True)

fig.add_trace(trace1, row=1, col=1)
fig.add_trace(trace2, row=1, col=2)
fig.add_trace(trace3, row=1, col=3)

fig['layout'].update(title='Temps for 3 cities')

pyo.plot(fig, filename='../charts/31_heatmaps_2.html')