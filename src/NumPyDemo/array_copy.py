# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-7-4
# update date: 2023-7-4
# function: demo for study numpy 拷贝


import numpy as np


def demo_0():
    a = np.arange(6)
    print('我们的数组是：')
    print(a)
    print('调用 id() 函数：')
    print(id(a))
    print('a 赋值给 b：')
    b = a
    print(b)
    print('b 拥有相同 id()：')
    print(id(b))
    print('修改 b 的形状：')
    b.shape = 3, 2
    print(b)
    print('a 的形状也修改了：')
    print(a)


def demo_view():
    # ndarray.view() 方会创建一个新的数组对象，该方法创建的新数组的维数变化不会改变原始数据的维数
    # 最开始 a 是个 3X2 的数组
    a = np.arange(6).reshape(3, 2)
    print('数组 a：')
    print(a)
    print('创建 a 的视图：')
    b = a.view()
    print(b)
    print('两个数组的 id() 不同：')
    print('a 的 id()：')
    print(id(a))
    print('b 的 id()：')
    print(id(b))
    # 修改 b 的形状，并不会修改 a
    b.shape = 2, 3
    print('b 的形状：')
    print(b)
    print('a 的形状：')
    print(a)


def demo_1():
    # 使用切片创建视图修改数据会影响到原始数组
    arr = np.arange(12)
    print('我们的数组：')
    print(arr)
    print('创建切片：')
    a = arr[3:]
    b = arr[3:]
    a[1] = 123
    b[2] = 234
    print(arr)
    print(id(a), id(b), id(arr[3:]))


def demo_copy():
    # ndarray.copy() 函数创建一个副本。 对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置
    a = np.array([[10, 10], [2, 3], [4, 5]])
    print('数组 a：')
    print(a)
    print('创建 a 的深层副本：')
    b = a.copy()
    print('数组 b：')
    print(b)
    # b 与 a 不共享任何内容
    print('我们能够写入 b 来写入 a 吗？')
    print(b is a)
    print('修改 b 的内容：')
    b[0, 0] = 100
    print('修改后的数组 b：')
    print(b)
    print('a 保持不变：')
    print(a)


def demo_2():
    a = np.arange(1, 12, 2)
    print(a)
    b = a.view()
    print("id(a) == id(b) ? %d" % id(a) == id(b))
    print("a的id=%d" % id(a))
    print("b的id=%d" % id(b))
    print(id(a[0]) == id(b[0]))
    print("a[0]的id=%d" % id(a[0]))
    print("b[0]的id=%d" % id(b[0]))
    print("reshape数组:", end="")
    b.shape = 2, 3
    print(b)
    print("原数组:", end="")
    print(a)
    print("替换元素:", end="")
    b[0][0] = -1
    print(b)
    print("原数组:", end="")
    print(a)


if __name__ == "__main__":
    # demo_0()
    # demo_view()
    # demo_1()
    # demo_copy()
    demo_2()
