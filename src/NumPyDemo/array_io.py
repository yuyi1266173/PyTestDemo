# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-7-4
# update date: 2023-7-4
# function: demo for study numpy.IO


import numpy as np


def demo_save():
    a = np.array([1, 2, 3, 4, 5])

    # 保存到 outfile.npy 文件上
    np.save('outfile.npy', a)

    # 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
    np.save('outfile2', a)


def demo_load():
    b = np.load('outfile.npy')
    print(b)


def demo_save_z():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.arange(0, 1.0, 0.1)
    c = np.sin(b)
    # c 使用了关键字参数 sin_array
    np.savez("runoob.npz", a, b, sin_array=c)
    r = np.load("runoob.npz")
    print(r.files)  # 查看各个数组名称
    print(r["arr_0"])  # 数组 a
    print(r["arr_1"])  # 数组 b
    print(r["sin_array"])  # 数组 c


def demo_save_txt():
    # a = np.array([1, 2, 3, 4, 5])
    # np.savetxt('out.txt', a)
    # b = np.loadtxt('out.txt')
    #
    # print(b)

    a = np.arange(0, 10, 0.5).reshape(4, -1)
    np.savetxt("out.txt", a, fmt="%d", delimiter=",")  # 改为保存为整数，以逗号分隔
    b = np.loadtxt("out.txt", delimiter=",")  # load 时也要指定为逗号分隔
    print(b)


if __name__ == "__main__":
    # demo_save()
    # demo_load()
    # demo_save_z()
    demo_save_txt()
