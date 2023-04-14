import plotly.graph_objs as go
import plotly.offline as pyo

# Dados para o gráfico
x = ['A', 'B', 'C', 'D']
y1 = [10, 20, 30, 40]
y2 = [20, 30, 10, 50]
y3 = [-5, -15, -25, -35]

# Criando o gráfico de barras empilhadas com valores relativos
data = [go.Bar(x=y1, y=x, name='Conjunto de dados 1', orientation='h'),
        go.Bar(x=y2, y=x, name='Conjunto de dados 2', orientation='h'),
        go.Bar(x=y3, y=x, name='Conjunto de dados 3', orientation='h')]

# Definindo o layout do gráfico
layout = go.Layout(title='Gráfico de barras empilhadas com valores relativos',
                   barmode='relative')

fig = go.Figure(data=data, layout=layout)

# Exibindo o gráfico
pyo.plot(fig, filename='../charts/relative_stacked_bar_chart_2.html')