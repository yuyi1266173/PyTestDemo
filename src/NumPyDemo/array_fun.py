# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-6-28
# update date: 2023-6-28
# function: demo for study Numpy 数组操作


import numpy as np


def demo_reshape():
    a = np.arange(8)
    print('原始数组：')
    print(a)
    b = a.reshape(4, 2)
    print('修改后的数组：')
    print(b)


def demo_flat():
    a = np.arange(9).reshape(3, 3)
    print('原始数组：\n', a)

    # 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
    print('迭代后的数组：')
    # numpy.ndarray.flat 是一个数组元素迭代器
    for element in a.flat:
        print(element)


def demo_flatten():
    # numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组

    a = np.arange(8).reshape(2, 4)

    print('原数组：')
    print(a)
    # 默认按行
    print('展开的数组：')
    print(a.flatten())
    print('以 F 风格顺序展开的数组：')
    print(a.flatten(order='F'))


def demo_ravel():
    # numpy.ravel() 展平的数组元素    order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
    a = np.arange(8).reshape(2, 4)

    print('原数组：')
    print(a)

    print('调用 ravel 函数之后：')
    print(a.ravel())

    print('以 F 风格顺序调用 ravel 函数之后：')
    print(a.ravel(order='F'))


def demo_transpose():
    # numpy.transpose 函数用于对换数组的维度    转置
    a = np.arange(12).reshape(3, 4)

    print('原数组：')
    print(a)

    print('对换数组：')
    print(np.transpose(a))
    print('转置数组：')
    print(a.T)


def demo_rollaxis():
    # 创建了三维的 ndarray
    a = np.arange(8).reshape(2, 2, 2)

    print('原数组：')
    print(a)
    print('获取数组中一个值：')
    print(np.where(a == 6))
    print(a[1, 1, 0])  # 为 6

    # 将轴 2 滚动到轴 0（宽度到深度）
    print('调用 rollaxis 函数：')
    b = np.rollaxis(a, 2, 0)
    print(b)
    # 查看元素 a[1,1,0]，即 6 的坐标，变成 [0, 1, 1]
    # 最后一个 0 移动到最前面
    print(np.where(b == 6))

    # 将轴 2 滚动到轴 1：（宽度到高度）
    print('调用 rollaxis 函数：')
    c = np.rollaxis(a, 2, 1)
    print(c)
    # 查看元素 a[1,1,0]，即 6 的坐标，变成 [1, 0, 1]
    # 最后的 0 和 它前面的 1 对换位置
    print(np.where(c == 6))
    print('\n')


def demo_swapaxes():
    # 创建了三维的 ndarray
    a = np.arange(8).reshape(2, 2, 2)

    print('原数组：')
    print(a)
    # 现在交换轴 0（深度方向）到轴 2（宽度方向）
    print('调用 swapaxes 函数后的数组：')
    print(np.swapaxes(a, 2, 0))


def demo_broadcast():
    x = np.array([[1], [2], [3]])
    y = np.array([4, 5, 6])

    # 对 y 广播 x
    b = np.broadcast(x, y)
    # 它拥有 iterator 属性，基于自身组件的迭代器元组
    print("b:", b)

    print('对 y 广播 x：')
    r, c = b.iters

    # Python3.x 为 next(context) ，Python2.x 为 context.next()
    print(next(r), next(c))
    print(next(r), next(c))
    # shape 属性返回广播对象的形状

    print('广播对象的形状：')
    print(b.shape)
    # 手动使用 broadcast 将 x 与 y 相加
    b = np.broadcast(x, y)
    c = np.empty(b.shape)

    print('手动使用 broadcast 将 x 与 y 相加：')
    print(c.shape)
    c.flat = [u + v for (u, v) in b]

    print('调用 flat 函数：')
    print(c)
    # 获得了和 NumPy 内建的广播支持相同的结果

    print('x 与 y 的和：')
    print(x + y)


def demo_broadcast_to():
    a = np.arange(4).reshape(1, 4)

    print('原数组：')
    print(a)

    print('调用 broadcast_to 函数之后：')
    print(np.broadcast_to(a, (4, 4)))


def demo_expand_dims():
    x = np.array(([1, 2], [3, 4]))
    print('数组 x：')
    print(x)

    y = np.expand_dims(x, axis=0)
    print('数组 y：')
    print(y)

    print('数组 x 和 y 的形状：')
    print(x.shape, y.shape)

    # 在位置 1 插入轴
    y = np.expand_dims(x, axis=1)
    print('在位置 1 插入轴之后的数组 y：')
    print(y)
    print('x.ndim 和 y.ndim：')
    print(x.ndim, y.ndim)
    print('x.shape 和 y.shape：')
    print(x.shape, y.shape)


def demo_squeeze():
    x = np.arange(9).reshape(1, 3, 3)
    print('数组 x：')
    print(x)

    # 从给定数组的形状中删除一维的条目
    y = np.squeeze(x)
    print('数组 y：')
    print(y)

    print('数组 x 和 y 的形状：')
    print(x.shape, y.shape)


def demo_concatenate():
    a = np.array([[1, 2], [3, 4]])
    print('第一个数组：')
    print(a)

    b = np.array([[5, 6], [7, 8]])
    print('第二个数组：')
    print(b)

    # 两个数组的维度相同
    print('沿轴 0 连接两个数组：')
    print(np.concatenate((a, b)))

    print('沿轴 1 连接两个数组：')
    print(np.concatenate((a, b), axis=1))


def demo_stack():
    a = np.array([[1, 2], [3, 4]])
    print('第一个数组：')
    print(a)

    b = np.array([[5, 6], [7, 8]])
    print('第二个数组：')
    print(b)

    print('沿轴 0 堆叠两个数组：')
    print(np.stack((a, b), 0))

    print('沿轴 1 堆叠两个数组：')
    print(np.stack((a, b), 1))


def demo_hstack():
    a = np.array([[1, 2], [3, 4]])
    print('第一个数组：')
    print(a)

    b = np.array([[5, 6], [7, 8]])
    print('第二个数组：')
    print(b)

    print('水平堆叠：')
    c = np.hstack((a, b))
    print(c)


def demo_vstack():
    a = np.array([[1, 2], [3, 4]])
    print('第一个数组：')
    print(a)

    b = np.array([[5, 6], [7, 8]])
    print('第二个数组：')
    print(b)

    print('竖直堆叠：')
    c = np.vstack((a, b))
    print(c)


def demo_split():
    a = np.arange(9)
    print('第一个数组：')
    print(a)

    print('将数组分为三个大小相等的子数组：')
    b = np.split(a, 3)
    print(b)

    print('将数组在一维数组中表明的位置分割：')
    b = np.split(a, [4, 7])
    print(b)


def demo_split_2():
    a = np.arange(16).reshape(4, 4)
    print('第一个数组：')
    print(a)

    print('默认分割（0轴）：')
    b = np.split(a, 2)
    print(b)

    print('沿水平方向分割：')
    c = np.split(a, 2, 1)
    print(c)

    print('沿水平方向分割：')
    d = np.hsplit(a, 2)
    print(d)


def demo_hsplit():
    h_arr = np.floor(10 * np.random.random((2, 6)))
    print('原array：')
    print(h_arr)

    print('拆分后：')
    print(np.hsplit(h_arr, 3))


def demo_vsplit():
    a = np.arange(16).reshape(4, 4)
    print('第一个数组：')
    print(a)

    print('竖直分割：')
    b = np.vsplit(a, 2)
    print(b)


def demo_resize():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print('第一个数组：')
    print(a)

    print('第一个数组的形状：')
    print(a.shape)
    b = np.resize(a, (3, 2))

    print('第二个数组：')
    print(b)

    print('第二个数组的形状：')
    print(b.shape)
    # 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了

    print('修改第二个数组的大小：')
    b = np.resize(a, (3, 3))
    print(b)


def demo_append():
    a = np.array([[1, 2, 3], [4, 5, 6]])

    print('第一个数组：')
    print(a)

    print('向数组添加元素：')
    print(np.append(a, [7, 8, 9]))

    print('沿轴 0 添加元素：')
    print(np.append(a, [[7, 8, 9]], axis=0))

    print('沿轴 1 添加元素：')
    print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))


def demo_insert():
    a = np.array([[1, 2], [3, 4], [5, 6]])
    print('第一个数组：')
    print(a)

    print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
    print(np.insert(a, 3, [11, 12]))

    print('传递了 Axis 参数。 会广播值数组来配输入数组。')
    print('沿轴 0 广播：')
    print(np.insert(a, 1, [11], axis=0))

    print('沿轴 1 广播：')
    print(np.insert(a, 1, 11, axis=1))


def demo_delete():
    a = np.arange(12).reshape(3, 4)
    print('第一个数组：')
    print(a)

    print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
    print(np.delete(a, 5))

    print('删除第二列：')
    print(np.delete(a, 1, axis=1))

    print('包含从数组中删除的替代值的切片：')
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(np.delete(a, np.s_[::2]))


def demo_unique():
    a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
    print('第一个数组：')
    print(a)

    print('第一个数组的去重值：')
    u = np.unique(a)
    print(u)

    print('去重数组的索引数组：')
    u, indices = np.unique(a, return_index=True)
    print(indices)

    print('我们可以看到每个和原数组下标对应的数值：')
    print(a)

    print('去重数组的下标：')
    u, indices = np.unique(a, return_inverse=True)
    print(u)

    print('下标为：')
    print(indices)

    print('使用下标重构原数组：')
    print(u[indices])
    print('\n')

    print('返回去重元素的重复数量：')
    u, indices = np.unique(a, return_counts=True)
    print(u)
    print(indices)


if __name__ == "__main__":
    # demo_reshape()
    # demo_flat()
    # demo_flatten()
    # demo_ravel()
    # demo_transpose()
    # demo_rollaxis()
    # demo_swapaxes()
    # demo_broadcast()
    # demo_broadcast_to()
    # demo_unique()
    # demo_delete()
    # demo_insert()
    # demo_append()
    # demo_resize()
    # demo_vsplit()
    # demo_hsplit()
    # demo_split()
    # demo_split_2()
    # demo_vstack()
    # demo_hstack()
    # demo_stack()
    # demo_concatenate()
    # demo_squeeze()
    demo_expand_dims()
