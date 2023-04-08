import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../data/2010YumaAZ.csv')
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']

print(df.head())

data = []

for day in days:
    df2 = df[df['DAY'] == day]
    df2.set_index('LST_TIME', inplace=True)

    trace = go.Scatter(
        x=df2.index,
        y=df2['T_HR_AVG'],
        mode='lines+markers',
        name=day
    )
    data.append(trace)

layout = go.Layout(
    title='Temperature chart per day of week',
    xaxis=dict(title='Hour'),
    yaxis=dict(title='Temperature'),
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, "14_line_charts_exercise.html")
