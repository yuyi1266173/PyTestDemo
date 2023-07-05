# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-6-27
# update date: 2023-6-27
# function: demo for study numpy.array

import numpy as np


def demo_1():
    a = np.array([1, 2, 3])
    print(a)

    a = np.array([[1, 2], [3, 4]])
    print(a)

    # ndmin: 指定生成数组的最小维度
    a = np.array([1, 2, 3], ndmin=2)
    print(a)

    # dtype: 数组元素的数据类型
    a = np.array([1, 2, 3], dtype=complex)
    print(a)


def demo_2():
    dt = np.dtype(np.int32)
    print(dt)

    # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
    dt = np.dtype('i4')
    print(dt)

    # 字节顺序标注
    dt = np.dtype('<i4')
    # dt = np.dtype('>i4')
    print(dt)

    # 创建结构化数据类型
    dt = np.dtype([('age', np.int8)])
    a = np.array([(10,), (20,), (30,)], dtype=dt)
    print(a)
    print(a['age'])

    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    print(student)
    a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
    print(a)


def demo_3():
    a = np.arange(24)
    print(a.ndim, a.shape)  # a 现只有一个维度
    # 现在调整其大小
    b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
    print(b)
    print(b.ndim, b.shape)

    x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
    print(x.itemsize)
    y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
    print(y.itemsize)


def demo_4():
    x_a = np.empty([3, 2], dtype=int)
    print(x_a)

    # np.zeros
    # 默认为浮点数
    x = np.zeros(5)
    print(x)
    # 设置类型为整数
    y = np.zeros((5,), dtype=int)
    print(y)
    # 自定义类型
    z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
    print(z)

    # np.ones
    # 默认为浮点数
    x = np.ones(5)
    print(x)
    # 自定义类型
    x = np.ones([2, 2], dtype=int)
    print(x)

    # np.zeros_like
    # 创建一个 3x3 的二维数组
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # 创建一个与 arr 形状相同的，所有元素都为 0 的数组
    zeros_arr = np.zeros_like(arr)
    print(zeros_arr)

    # np.ones_like
    # 创建一个 3x3 的二维数组
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # 创建一个与 arr 形状相同的，所有元素都为 1 的数组
    ones_arr = np.ones_like(arr)
    print(ones_arr)


def demo_5():
    # np.asarray
    # x = [1, 2, 3]
    # x = (1, 2, 3)
    x = [(1, 2, 3), (4, 5, 6)]
    a = np.asarray(x)
    print(a)
    x = [1, 2, 3]
    a = np.asarray(x, dtype=float)
    print(a)

    # np.frombuffer
    s = b'Hello World'
    # s = 'Hello World'
    a = np.frombuffer(s, dtype='S1')
    print(a)

    # np.fromiter
    # 使用 range 函数创建列表对象
    it = iter(range(5))
    # 使用迭代器创建 ndarray
    x = np.fromiter(it, dtype=float)
    print(x)


def demo_6():
    # np.arange
    x = np.arange(5)
    print(x)
    # 设置了 dtype
    x = np.arange(5, dtype=float)
    print(x)
    x = np.arange(10, 20, 2)
    print(x)

    # numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的
    a = np.linspace(1, 10, 10)
    print(a)
    a = np.linspace(1, 1, 10)
    print(a)
    # 将 endpoint 设为 false，不包含终止值
    a = np.linspace(10, 20, 5, endpoint=False)
    # a = np.linspace(10, 20, 5)
    print(a)
    # retstep 为 True 时，生成的数组中会显示间距，反之不显示
    a = np.linspace(1, 10, 10, retstep=True)
    print(a)
    b = np.linspace(1, 10, 10).reshape([10, 1])
    print(b)

    # numpy.logspace 函数用于创建一个于等比数列
    # 默认底数是 10
    a = np.logspace(1.0, 2.0, num=10)
    print(a)
    a = np.logspace(0, 9, 10, base=2)
    print(a)


def demo_slice():
    a = np.arange(10)
    s = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2
    print(a[s])

    a = np.arange(10)
    b = a[2:7:2]  # 从索引 2 开始到索引 7 停止，间隔为 2
    print(b)
    c = a[5]
    print(c)
    print(a[2:])
    print(a[2:5])

    a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    print(a)
    # 从某个索引处开始切割
    print('从数组索引 a[1:] 处开始切割')
    print(a[1:])
    print(a[..., 1])  # 第2列元素
    print(a[1, ...])  # 第2行元素
    print(a[..., 1:])  # 第2列及剩下的所有元素
    print(a[0:2, 1:3])


def demo_slice_2():
    # 整数数组索引
    x = np.array([[1, 2], [3, 4], [5, 6]])
    y = x[[0, 1, 2], [0, 1, 0]]
    print(y)
    print("==============================")

    x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    print('我们的数组是：')
    print(x)
    rows = np.array([[0, 0], [3, 3]])
    cols = np.array([[0, 2], [0, 2]])
    y = x[rows, cols]
    print('这个数组的四个角元素是：')
    print(y)

    y = x[[0, 3], :][:, [0, 2]]  # 生成一个二维数组：取第一行第一列、第一行第3列 和 第4行第一列、第4行第三列的数
    print(y)
    print("==============================")

    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = a[1:3, 1:3]
    c = a[1:3, [1, 2]]
    d = a[..., 1:]
    print(b)
    print(c)
    print(d)
    print("==============================")

    # 布尔索引
    x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    print('我们的数组是：')
    print(x)
    # 现在我们会打印出大于 5 的元素
    print('大于 5 的元素是：')
    print(x[x > 5])

    a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
    print(a[~np.isnan(a)])

    a = np.array([1, 2 + 6j, 5, 3.5 + 5j])
    print(a[np.iscomplex(a)])

    # 花式索引
    x = np.arange(9)
    print(x)
    # 一维数组读取指定下标对应的元素
    print("-------读取下标对应的元素-------")
    x2 = x[[0, 6]]  # 使用花式索引
    print(x2)
    print(x2[0])
    print(x2[1])

    print("=================================")
    x = np.arange(32).reshape((8, 4))
    print(x)
    # 二维数组读取指定下标对应的行
    print("-------读取下标对应的行-------")
    print(x[[4, 2, 1, 7]])
    print(x[[-4, -2, -1, -7]])
    """
    x[1,0] x[1,3] x[1,1] x[1,2]
    x[5,0] x[5,3] x[5,1] x[5,2]
    x[7,0] x[7,3] x[7,1] x[7,2]
    x[2,0] x[2,3] x[2,1] x[2,2]
    """
    print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
    print("=================================")


def demo_slice_3():
    x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    print('原数组：\n', x)
    print('大于5且小于10的元素：')
    print('条件加小括号：')
    print(x[(x > 5) & (x < 10)])
    print('使用np.logical_and方法：')
    print(x[np.logical_and(x > 5, x < 10)])
    print('使用np.all方法：')
    print(x[np.all([x > 5, x < 10], axis=0)])

    print("==================================")
    a = np.array([[1, 1, 0],
                  [2, 1, 0],
                  [3, 2, 0],
                  [4, 2, 0],
                  [5, 3, 0]])
    b = a[(a[..., 0] > 2) & (a[..., 1] < 3), ...]  # 此行的最后的逗号和省略号可以省略
    print(b)


if __name__ == "__main__":
    # demo_1()
    # demo_2()
    # demo_3()
    # demo_4()
    # demo_5()
    # demo_6()
    # demo_slice()
    demo_slice_2()
    # demo_slice_3()
