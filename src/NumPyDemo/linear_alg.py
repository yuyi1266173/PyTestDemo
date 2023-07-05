# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-7-4
# update date: 2023-7-4
# function: demo for study numpy.线性代数


import numpy as np


def demo_dot():
    # 两个数组的点积，即元素对应相乘。
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[11, 12], [13, 14]])
    # [[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
    print(np.dot(a, b))


def demo_vdot():
    # numpy.vdot() 函数是两个向量的点积
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[11, 12], [13, 14]])

    # vdot 将数组展开计算内积
    # 1*11 + 2*12 + 3*13 + 4*14 = 130
    print(np.vdot(a, b))


def demo_inner():
    # numpy.inner() 函数返回一维数组的向量内积, 对于更高的维度，它返回最后一个轴上的和的乘积。
    print(np.inner(np.array([1, 2, 3]), np.array([0, 1, 0])))
    # 等价于 1*0+2*1+3*0

    a = np.array([[1, 2], [3, 4]])
    print('数组 a：')
    print(a)
    b = np.array([[11, 12], [13, 14]])
    print('数组 b：')
    print(b)
    print('内积：')
    # 1*11+2*12, 1*13+2*14
    # 3*11+4*12, 3*13+4*14
    print(np.inner(a, b))


def demo_matmul():
    a = [[1, 0], [0, 1]]
    b = [[4, 1], [2, 2]]
    print(np.matmul(a, b))
    print("==============================")

    a = [[1, 0], [0, 1]]
    b = [1, 2]
    print(np.matmul(a, b))
    print(np.matmul(b, a))
    print("==============================")

    a = np.arange(8).reshape(2, 2, 2)
    b = np.arange(4).reshape(2, 2)
    print(np.matmul(a, b))


def demo_det():
    a = np.array([[1, 2], [3, 4]])

    # numpy.linalg.det() 函数计算输入矩阵的行列式
    # 对于矩阵[[a，b]，[c，d]]，行列式计算为 ad-bc
    print(np.linalg.det(a))

    b = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
    print(b)
    print(np.linalg.det(b))
    print(6 * (-2 * 7 - 5 * 8) - 1 * (4 * 7 - 5 * 2) + 1 * (4 * 8 - -2 * 2))


def demo_inv():
    # numpy.linalg.inv() 函数计算矩阵的乘法逆矩阵
    x = np.array([[1, 2], [3, 4]])
    y = np.linalg.inv(x)
    print(x)
    print(y)
    print(np.dot(x, y))

    print("==============================")
    a = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
    print('数组 a：')
    print(a)

    ainv = np.linalg.inv(a)
    print('a 的逆：')
    print(ainv)

    print('矩阵 b：')
    b = np.array([[6], [-4], [27]])
    print(b)

    print('计算：A^(-1)B：')
    x = np.linalg.solve(a, b)
    print(x)
    # 这就是线性方向 x = 5, y = 3, z = -2 的解


if __name__ == "__main__":
    # demo_dot()
    # demo_vdot()
    # demo_inner()
    # demo_matmul()
    # demo_det()
    demo_inv()
