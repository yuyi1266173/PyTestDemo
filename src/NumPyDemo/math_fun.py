# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-6-30
# update date: 2023-6-30
# function: demo for study numpy 字符串函数


import numpy as np


def demo_1():
    a = np.array([0, 30, 45, 60, 90])
    print('不同角度的正弦值：')
    # 通过乘 pi/180 转化为弧度
    print(np.sin(a * np.pi / 180))
    print('\n')
    print('数组中角度的余弦值：')
    print(np.cos(a * np.pi / 180))
    print('\n')
    print('数组中角度的正切值：')
    print(np.tan(a * np.pi / 180))


def demo_2():
    a = np.array([0, 30, 45, 60, 90])
    print('含有正弦值的数组：')
    sin = np.sin(a * np.pi / 180)
    print(sin)
    print('计算角度的反正弦，返回值以弧度为单位：')
    inv = np.arcsin(sin)
    print(inv)
    print('通过转化为角度制来检查结果：')
    print(np.degrees(inv))
    print('\n')
    print('arccos 和 arctan 函数行为类似：')
    cos = np.cos(a * np.pi / 180)
    print(cos)
    print('反余弦：')
    inv = np.arccos(cos)
    print(inv)
    print('角度制单位：')
    print(np.degrees(inv))
    print('\n')
    print('tan 函数：')
    tan = np.tan(a * np.pi / 180)
    print(tan)
    print('反正切：')
    inv = np.arctan(tan)
    print(inv)
    print('角度制单位：')
    print(np.degrees(inv))


def demo_around():
    a = np.array([1.0, 5.55, 123, 0.567, 25.532])
    print('原数组：')
    print(a)
    print('舍入后：')
    print(np.around(a))
    print(np.around(a, decimals=1))
    print(np.around(a, decimals=-1))


def demo_floor():
    a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
    print('提供的数组：')
    print(a)
    print('修改后的数组：')
    print(np.floor(a))


def demo_ceil():
    a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
    print('提供的数组：')
    print(a)
    print('修改后的数组：')
    print(np.ceil(a))


def demo_3():
    a = np.arange(9, dtype=np.float_).reshape(3, 3)
    print('第一个数组：')
    print(a)
    print('第二个数组：')
    b = np.array([10, 10, 10])
    print(b)

    print('两个数组相加：')
    print(np.add(a, b))

    print('两个数组相减：')
    print(np.subtract(a, b))

    print('两个数组相乘：')
    print(np.multiply(a, b))

    print('两个数组相除：')
    print(np.divide(a, b))


def demo_4():
    # numpy.reciprocal() 函数返回参数逐元素的倒数。如 1/4 倒数为 4/1。
    a = np.array([0.25, 1.33, 1, 100])
    print('我们的数组是：')
    print(a)
    print('调用 reciprocal 函数：')
    print(np.reciprocal(a))

    print("===============================================")
    # numpy.power() 函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂
    a = np.array([10, 100, 1000])
    print('我们的数组是；')
    print(a)
    print('调用 power 函数：')
    print(np.power(a, 2))
    print('第二个数组：')
    b = np.array([1, 2, 3])
    print(b)
    print('再次调用 power 函数：')
    print(np.power(a, b))

    print("===============================================")
    # numpy.mod() 计算输入数组中相应元素的相除后的余数。 函数 numpy.remainder() 也产生相同的结果
    a = np.array([10, 20, 30])
    b = np.array([3, 5, 7])
    print('第一个数组：')
    print(a)
    print('第二个数组：')
    print(b)
    print('调用 mod() 函数：')
    print(np.mod(a, b))
    print('调用 remainder() 函数：')
    print(np.remainder(a, b))


def demo_min_max():
    a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
    print('我们的数组是：')
    print(a)
    print('调用 amin() 函数：')
    print(np.amin(a, 1))
    print('再次调用 amin() 函数：')
    print(np.amin(a, 0))
    print('调用 amax() 函数：')
    print(np.amax(a))
    print('再次调用 amax() 函数：')
    print(np.amax(a, axis=0))


def demo_ptp():
    # numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值 - 最小值
    a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
    print('我们的数组是：')
    print(a)
    print('调用 ptp() 函数：')
    print(np.ptp(a))
    print('沿轴 1 调用 ptp() 函数：')
    print(np.ptp(a, axis=1))
    print('沿轴 0 调用 ptp() 函数：')
    print(np.ptp(a, axis=0))


def demo_percentile():
    a = np.array([[10, 7, 4], [3, 2, 1]])
    print('我们的数组是：')
    print(a)
    print('调用 percentile() 函数：')
    # 50% 的分位数，就是 a 里排序之后的中位数
    print(np.percentile(a, 50))
    # axis 为 0，在纵列上求
    print(np.percentile(a, 50, axis=0))
    # axis 为 1，在横行上求
    print(np.percentile(a, 50, axis=1))
    # 保持维度不变
    print(np.percentile(a, 50, axis=1, keepdims=True))


def demo_median():
    # numpy.median() 函数用于计算数组 a 中元素的中位数（中值）
    a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
    print('我们的数组是：')
    print(a)
    print('调用 median() 函数：')
    print(np.median(a))
    print('沿轴 0 调用 median() 函数：')
    print(np.median(a, axis=0))
    print('沿轴 1 调用 median() 函数：')
    print(np.median(a, axis=1))


def demo_mean():
    # numpy.mean() 函数返回数组中元素的   [算术平均值]
    a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    print('我们的数组是：')
    print(a)
    print('调用 mean() 函数：')
    print(np.mean(a))
    print('沿轴 0 调用 mean() 函数：')
    print(np.mean(a, axis=0))
    print('沿轴 1 调用 mean() 函数：')
    print(np.mean(a, axis=1))


def demo_average():
    # numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的  [加权平均值]
    a = np.array([1, 2, 3, 4])
    print('我们的数组是：')
    print(a)
    print('调用 average() 函数：')
    print(np.average(a))
    # 不指定权重时相当于 mean 函数
    wts = np.array([4, 3, 2, 1])
    print('再次调用 average() 函数：')
    print(np.average(a, weights=wts))
    # 如果 returned 参数设为 true，则返回权重的和
    print('权重的和：')
    print(np.average([1, 2, 3, 4], weights=[4, 3, 2, 1], returned=True))

    b = np.arange(6).reshape(3, 2)
    print('我们的数组是：')
    print(b)
    print('修改后的数组：')
    wt = np.array([3, 5])
    print(np.average(b, axis=1, weights=wt))
    print('修改后的数组：')
    print(np.average(b, axis=1, weights=wt, returned=True))


def demo_std():
    # std = sqrt(mean((x - x.mean())**2))
    print(np.std([1, 2, 3, 4]))


def demo_var():
    # mean((x - x.mean())** 2)
    print(np.var([1, 2, 3, 4]))


if __name__ == "__main__":
    # demo_1()
    # demo_2()
    # demo_around()
    # demo_floor()
    # demo_ceil()
    # demo_3()
    # demo_4()
    # demo_min_max()
    # demo_ptp()
    # demo_percentile()
    # demo_median()
    # demo_mean()
    # demo_average()
    demo_std()
    demo_var()
