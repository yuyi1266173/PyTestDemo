# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-6-30
# update date: 2023-6-30
# function: demo for study numpy 排序、条件筛选函数


import numpy as np


def demo_sort():
    a = np.array([[3, 7], [9, 1]])
    print('我们的数组是：')
    print(a)
    print('调用 sort() 函数：')
    print(np.sort(a))
    print('按列排序：')
    print(np.sort(a, axis=0))

    # 在 sort 函数中排序字段
    dt = np.dtype([('name', 'S10'), ('age', int)])
    a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
    print('我们的数组是：')
    print(a)
    print('按 name 排序：')
    print(np.sort(a, order='name'))


def demo_argsort():
    # numpy.argsort() 函数返回的是数组值从小到大的索引值
    x = np.array([3, 1, 2])
    print('我们的数组是：')
    print(x)
    print('对 x 调用 argsort() 函数：')
    y = np.argsort(x)
    print(y)
    print('以排序后的顺序重构原数组：')
    print(x[y])
    print('使用循环重构原数组：')
    for i in y:
        print(x[i], end=" ")


def demo_lexsort():
    nm = ('raju', 'anil', 'ravi', 'amar')
    dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
    ind = np.lexsort((dv, nm))
    print('调用 lexsort() 函数：')
    print(ind)
    print('使用这个索引来获取排序后的数据：')
    print([nm[i] + ", " + dv[i] for i in ind])


def demo_sort_complex():
    print(np.sort_complex([5, 3, 6, 2, 1]))
    print(np.sort_complex([1 + 2j, 2 - 1j, 3 - 2j, 3 - 3j, 3 + 5j]))


def demo_partition():
    a = np.array([3, 4, 2, 1])
    # 将数组 a 中所有元素（包括重复元素）从小到大排列，3表示的是排序数组索引为3的数字，比该数字小的排在该数字前面，比该数字大的排在该数字的后面
    print(np.partition(a, 3))
    # 小于 1 的在前面，大于 3 的在后面，1和3之间的在中间
    print(np.partition(a, (1, 3)))


def demo_argpartition():
    arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])

    # 找到数组的第 3 小（index=2）的值, 只对前三小的数字进行排序
    print(np.argpartition(arr, 2))
    print(arr[np.argpartition(arr, 2)])
    print(arr[np.argpartition(arr, 2)[2]])

    # 找到数组的第 2 大（index=-2）的值, 只对前两个大的数字进行排序
    print(arr[np.argpartition(arr, -2)])
    print(arr[np.argpartition(arr, -2)[-2]])

    # 同时找到第 3 和第 4 小的值
    print(np.argpartition(arr, [2, 3]))
    print(arr[np.argpartition(arr, [2, 3])])
    print(arr[np.argpartition(arr, [2, 3])[2]])
    print(arr[np.argpartition(arr, [2, 3])[3]])


def demo_arg_max_min():
    # 沿给定轴返回最大元素的索引
    a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
    print('我们的数组是：')
    print(a)
    print('调用 argmax() 函数：')
    print(np.argmax(a))
    print('展开数组：')
    print(a.flatten())
    print('沿轴 0 的最大值索引：')
    maxindex = np.argmax(a, axis=0)
    print(maxindex)
    print('沿轴 1 的最大值索引：')
    maxindex = np.argmax(a, axis=1)
    print(maxindex)
    print('调用 argmin() 函数：')
    minindex = np.argmin(a)
    print(minindex)
    print('展开数组中的最小值：')
    print(a.flatten()[minindex])
    print('沿轴 0 的最小值索引：')
    minindex = np.argmin(a, axis=0)
    print(minindex)
    print('沿轴 1 的最小值索引：')
    minindex = np.argmin(a, axis=1)
    print(minindex)


def demo_nonzero():
    # numpy.nonzero() 函数返回输入数组中 [非零元素] 的索引
    a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
    print('我们的数组是：')
    print(a)
    print('调用 nonzero() 函数：')
    print(np.nonzero(a))


def demo_where():
    x = np.arange(9.).reshape(3, 3)
    print('我们的数组是：')
    print(x)
    print('大于 3 的元素的索引：')
    y = np.where(x > 3)
    print(y)
    print('使用这些索引来获取满足条件的元素：')
    print(x[y])


def demo_extract():
    x = np.arange(9.).reshape(3, 3)
    print('我们的数组是：')
    print(x)
    # 定义条件, 选择偶数元素
    condition = np.mod(x, 2) == 0
    print('按元素的条件值：')
    print(condition)
    print('使用条件提取元素：')
    print(np.extract(condition, x))


if __name__ == "__main__":
    # demo_sort()
    # demo_argsort()
    # demo_lexsort()
    # demo_sort_complex()
    # demo_partition()
    # demo_argpartition()
    # demo_arg_max_min()
    # demo_nonzero()
    # demo_where()
    demo_extract()
