import plotly.graph_objs as go
import plotly.offline as pyo

# Dados para o gráfico
x = ['A', 'B', 'C', 'D']
y1 = [10, 20, 30, 40]
y2 = [20, 30, 10, 50]
y3 = [-5, -15, -25, -35]

fig = go.Figure()
fig.add_bar(x=y1, y=x, name='Conjunto de dados 1', orientation='h')
fig.add_bar(x=y2, y=x, name='Conjunto de dados 2', orientation='h')
fig.add_bar(x=y3, y=x, name='Conjunto de dados 3', orientation='h')

fig.update_layout(barmode='relative', title='Gráfico de barras empilhadas com valores relativos')

# Exibindo o gráfico
pyo.plot(fig, filename='../charts/relative_stacked_bar_chart_1.html')