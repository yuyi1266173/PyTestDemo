# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-6-28
# update date: 2023-6-28
# function: demo for study numpy.nditer


import numpy as np


def demo_1():
    a = np.arange(6).reshape(2, 3)
    print('原始数组是：')
    print(a)
    print('迭代输出元素：')
    for x in np.nditer(a):
        print(x, end=", ")
    print('\n')

    # a 和 a.T 的遍历顺序是一样的，也就是他们在内存中的存储顺序也是一样的
    for x in np.nditer(a.T):
        print(x, end=", ")
    print('\n')

    #  a.T.copy(order = 'C') 的遍历结果是不同的，那是因为它和前两种的存储方式是不一样的，默认是按行访问。
    for x in np.nditer(a.T.copy(order='C')):
        print(x, end=", ")
    print('\n')


def demo_2():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print('原始数组是：')
    print(a)
    print('原始数组的转置是：')
    b = a.T
    print(b)
    print('以 C 风格顺序排序：')
    c = b.copy(order='C')
    print(c)
    for x in np.nditer(c):
        print(x, end=", ")
    print('\n')
    print('以 F 风格顺序排序：')
    c = b.copy(order='F')
    print(c)
    for x in np.nditer(c):
        print(x, end=", ")


def demo_3():
    # 可以通过显式设置，来强制 nditer 对象使用某种顺序
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print('原始数组是：')
    print(a)
    print('以 C 风格顺序排序：')
    for x in np.nditer(a, order='C'):
        print(x, end=", ")
    print('\n')

    print('以 F 风格顺序排序：')
    for x in np.nditer(a, order='F'):
        print(x, end=", ")


def demo_4():
    """
     默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），为了在遍历数组的同时，实现对数组元素值得修改，
     必须指定 readwrite 或者 writeonly 的模式。
    """
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print('原始数组是：')
    print(a)
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...] = 2 * x
    print('修改后的数组是：')
    print(a)


def demo_5():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print('原始数组是：')
    print(a)
    print('\n')
    # external_loop 给出的值是具有多个值的一维数组，而不是零维数组
    for x in np.nditer(a, flags=['external_loop'], order='F'):
        print(x, end=", ")


def demo_6():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print('第一个数组为：')
    print(a)
    print('第二个数组为：')
    b = np.array([1, 2, 3, 4], dtype=int)
    print(b)
    print('np.nditer([a, b])：')
    for x, y in np.nditer([a, b]):
        print("%d:%d" % (x, y), end=", ")


if __name__ == "__main__":
    # demo_1()
    # demo_2()
    # demo_3()
    # demo_4()
    # demo_5()
    demo_6()
