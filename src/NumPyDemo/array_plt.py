# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-7-5
# update date: 2023-7-5
# function: demo for study numpy Matplotlib


import numpy as np
import matplotlib
from matplotlib import pyplot as plt


def demo_1():
    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y)
    plt.show()


def demo_2():
    # fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径
    zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")

    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("菜鸟教程 - 测试", fontproperties=zhfont1)
    # fontproperties 设置中文显示，fontsize 设置字体大小
    plt.xlabel("x 轴", fontproperties=zhfont1)
    plt.ylabel("y 轴", fontproperties=zhfont1)
    plt.plot(x, y)
    plt.show()


def demo_3():
    a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

    for i in a:
        print(i)

    plt.rcParams['font.family'] = ['STFangsong']

    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("菜鸟教程 - 测试")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")
    plt.plot(x, y)
    plt.show()


def demo_4():
    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y, "ob")
    plt.show()


def demo_5():
    # 计算正弦曲线上点的 x 和 y 坐标
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.title("sine wave form")
    # 使用 matplotlib 来绘制点
    plt.plot(x, y)
    plt.show()


def demo_6():
    # 计算正弦和余弦曲线上的点的 x 和 y 坐标
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    # 建立 subplot 网格，高为 2，宽为 1
    # 激活第一个 subplot
    plt.subplot(2, 1, 1)
    # 绘制第一个图像
    plt.plot(x, y_sin)
    plt.title('Sine')
    plt.xlabel("sin-x axis caption")
    plt.ylabel("sin-y axis caption")
    # 将第二个 subplot 激活，并绘制第二个图像
    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')
    plt.xlabel("cos-x axis caption")
    plt.ylabel("cos-y axis caption")
    # 展示图像
    plt.show()


def demo_7():
    x = [5, 8, 10]
    y = [12, 16, 6]
    x2 = [6, 9, 11]
    y2 = [6, 15, 7]
    plt.bar(x, y, align='center')
    plt.bar(x2, y2, color='g', align='center')
    plt.title('Bar graph')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()


if __name__ == "__main__":
    # demo_1()
    # demo_2()
    # demo_3()
    # demo_4()
    # demo_5()
    # demo_6()
    demo_7()
