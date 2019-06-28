# ! /usr/bin/python3
# -*- coding: utf-8 -*-

from pyecharts.charts import Bar
from pyecharts import options as opts


def show_bar():
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
    y1 = [5, 20, 36, 10, 75]
    y2 = [10, 25, 8, 60, 20]

    bar = Bar()
    bar.add_xaxis(x)
    bar.add_yaxis("商家A", yaxis_data=y1)
    bar.add_yaxis("商家B", yaxis_data=y2)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))

    bar.render('柱形图示范.html')


if __name__ == "__main__":
    show_bar()

