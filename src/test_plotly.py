import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as pltoff


def test():
    """折线图"""
    trace1 = go.Scatter(
        x=[1, 2, 3, 4, 5,
           6, 7, 8, 9, 10,
           11, 12, 13, 14, 15],
        y=[10, 20, None, 15, 10,
           5, 15, None, 20, 10,
           10, 15, 25, 20, 10],
        name='<b>No</b> Gaps',  # Style name/legend entry with html tags
        connectgaps=True)

    trace2 = go.Scatter(
        x=[1, 2, 3, 4, 5,
           6, 7, 8, 9, 10,
           11, 12, 13, 14, 15],
        y=[5, 15, None, 10, 5,
           0, 10, None, 15, 5,
           5, 10, 20, 15, 5],
        name='Gaps', )

    data = [trace1, trace2]
    fig = dict(data=data)
    pltoff.plot(fig, filename='simple-connectgaps.html')


def scatter_plots(name):
    """绘制散点图"""
    dataset = {'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
               'y': [5, 4, 1, 3, 11, 2, 6, 7, 19, 20],
               'text': ['5_txt', '4_txt', '1_txt', '3_txt', '11_txt', '2_txt', '6_txt', '7_txt', '19_txt', '20_txt']
               }
    data_g = []
    tr_x = go.Scatter(
        x=dataset['x'],
        y=dataset['y'],
        text=dataset['text'],
        textposition='top center',
        mode='markers+text',
        name='y')
    data_g.append(tr_x)
    layout = go.Layout(title="scatter plots", xaxis={'title': 'x'}, yaxis={'title': 'value'})
    fig = go.Figure(data=data_g, layout=layout)
    pltoff.plot(fig, filename=name)


def bar_charts(name):
    """绘制柱状图"""
    dataset = {
        'x': ['Windows', 'Linux', 'Unix', 'MacOS'],
        'y1': [45, 26, 37, 13],
        'y2': [19, 27, 33, 21]
    }
    data_g = []
    tr_y1 = go.Bar(x=dataset['x'], y=dataset['y1'], name='v1')
    data_g.append(tr_y1)
    tr_y2 = go.Bar(x=dataset['x'], y=dataset['y2'], name='v2')
    data_g.append(tr_y2)
    layout = go.Layout(title="bar charts", xaxis={'title': 'x'}, yaxis={'title': 'value'})
    fig = go.Figure(data=data_g, layout=layout)
    pltoff.plot(fig, filename=name)


def pie_charts(name):
    """绘制饼图"""
    dataset = {'labels': ['Windows', 'Linux', 'Unix', 'MacOS', 'Android', 'iOS'],
               'values': [280, 25, 10, 100, 250, 270]}
    data_g = []
    tr_p = go.Pie(labels=dataset['labels'], values=dataset['values'])
    data_g.append(tr_p)
    layout = go.Layout(title="pie charts")
    fig = go.Figure(data=data_g, layout=layout)
    pltoff.plot(fig, filename=name)


if __name__ == "__main__":
    # test()
    # scatter_plots("scatter_plots.html")
    # bar_charts("bar_charts.html")
    pie_charts("pie_charts.html")
