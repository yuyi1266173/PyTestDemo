# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-7-4
# update date: 2023-7-4
# function: demo for study numpy.矩阵库(Matrix)


import numpy as np


def demo_transpose():
    a = np.arange(12).reshape(3, 4)

    print('原数组：')
    print(a)

    print('转置数组：')
    print(a.T)


def demo_0():
    # empty() 函数返回一个新的矩阵
    print(np.empty((2, 2)))
    # 填充为随机数据

    # numpy.zeros() 函数创建一个以 0 填充的矩阵
    print(np.zeros((2, 2)))

    # numpy.ones()函数创建一个以 1 填充的矩阵
    print(np.ones((2, 2)))

    # numpy.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零
    print(np.eye(N=3, M=4, k=0, dtype=float))

    # numpy.identity() 函数返回给定大小的单位矩阵
    # 单位矩阵是个方阵，从左上角到右下角的对角线（称为主对角线）上的元素均为 1，除此以外全都为 0
    print(np.identity(5, dtype=float))

    #
    print(np.random.random((3, 3)))


if __name__ == "__main__":
    # demo_transpose()
    demo_0()
