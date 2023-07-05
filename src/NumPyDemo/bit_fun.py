# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-6-30
# update date: 2023-6-30
# function: demo for study numpy 位运算


import numpy as np


def demo_bitwise_and():
    print('13 和 17 的二进制形式：')
    a, b = 13, 17
    print(bin(a), bin(b))
    print('\n')

    print('13 和 17 的位与：')
    print(np.bitwise_and(13, 17))


def demo_bitwise_or():
    a, b = 13, 17
    print('13 和 17 的二进制形式：')
    print(bin(a), bin(b))

    print('13 和 17 的位或：')
    print(np.bitwise_or(13, 17))


def demo_invert():
    print('13 的位反转，其中 ndarray 的 dtype 是 uint8：')
    print(np.invert(np.array([13], dtype=np.uint8)))

    # 比较 13 和 242 的二进制表示，我们发现了位的反转
    print('13 的二进制表示：')
    print(np.binary_repr(13, width=8))

    print('242 的二进制表示：')
    print(np.binary_repr(242, width=8))


def demo_shift():
    print('将 10 左移两位：')
    print(np.left_shift(10, 2))

    print('10 的二进制表示：')
    print(np.binary_repr(10, width=8))

    print('40 的二进制表示：')
    print(np.binary_repr(40, width=8))
    #  '00001010' 中的两位移动到了左边，并在右边添加了两个 0。


def demo_right_shift():
    print('将 40 右移两位：')
    print(np.right_shift(40, 2))

    print('40 的二进制表示：')
    print(np.binary_repr(40, width=8))

    print('10 的二进制表示：')
    print(np.binary_repr(10, width=8))
    #  '00001010' 中的两位移动到了右边，并在左边添加了两个 0。


def demo_byte_swap():
    a = np.array([1, 256, 8755], dtype=np.int16)
    print('我们的数组是：')
    print(a)
    print('以十六进制表示内存中的数据：')
    print(list(map(hex, a)))
    # byteswap() 函数通过传入 true 来原地交换
    print('调用 byteswap() 函数：')
    print(a.byteswap(True))
    print('十六进制形式：')
    print(list(map(hex, a)))
    # 我们可以看到字节已经交换了


if __name__ == "__main__":
    # demo_bitwise_and()
    # demo_bitwise_or()
    # demo_invert()
    # demo_shift()
    # demo_right_shift()
    demo_byte_swap()
