# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-6-28
# update date: 2023-6-28
# function: demo for study numpy.broadcast


import numpy as np


def demo_1():
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])
    c = a * b
    print(c)

    print("=============================")
    a = np.array([[0, 0, 0],
                  [10, 10, 10],
                  [20, 20, 20],
                  [30, 30, 30]])
    b = np.array([0, 1, 2])
    print(a + b)

    print("=============================")
    bb = np.tile(b, (4, 1))  # np.tile横向、纵向的扩充数组
    print("bb:", bb)
    print(a + bb)


if __name__ == "__main__":
    demo_1()
