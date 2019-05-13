# ! /usr/bin/python3
# -*- coding: utf-8 -*-

from pyecharts import Bar


def test_bar():
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
    y1 = [5, 20, 36, 10, 75]
    y2 = [10, 25, 8, 60, 20]

    bar = Bar(title="产品月销量", width=600, height=420)
    bar.add(name="商家A", x_axis=x, y_axis=y1)
    bar.add(name="商家B", x_axis=x, y_axis=y2, is_xaxis_boundarygap=True)

    bar.render('柱形图示范.html')


if __name__ == "__main__":
    test_bar()

