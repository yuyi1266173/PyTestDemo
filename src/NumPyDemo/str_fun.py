# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-6-30
# update date: 2023-6-30
# function: demo for study numpy 字符串函数


import numpy as np


def demo_char_add():
    print('连接两个字符串：')
    print(np.char.add(['hello'], [' xyz']))

    print('连接示例：')
    print(np.char.add(['hello', 'hi'], [' abc', ' xyz']))


def demo_char_1():
    print(np.char.multiply('Runoob ', 3))

    # np.char.center(str , width,fillchar) ：
    # str: 字符串，width: 长度，fillchar: 填充字符
    print(np.char.center('Runoob', 20, fillchar='*'))

    print(np.char.capitalize('runoob'))

    print(np.char.title('i like runoob'))

    # 操作数组
    print(np.char.lower(['RUNOOB', 'GOOGLE']))
    # 操作字符串
    print(np.char.lower('RUNOOB'))

    # 操作数组
    print(np.char.upper(['runoob', 'google']))
    # 操作字符串
    print(np.char.upper('runoob'))

    # 分隔符默认为空格
    print(np.char.split('i like runoob?'))
    # 分隔符为 .
    print(np.char.split('www.runoob.com', sep='.'))

    # 换行符 \n
    # \n，\r，\r\n 都可用作换行符。
    print(np.char.splitlines('i\nlike runoob?'))
    print(np.char.splitlines('i\rlike runoob?'))

    # 移除字符串头尾的 a 字符
    print(np.char.strip('ashok arunooba', 'a'))
    # 移除数组元素头尾的 a 字符
    print(np.char.strip(['arunooba', 'admin', 'java'], 'a'))

    # 操作字符串
    print(np.char.join(':', 'runoob'))
    # 指定多个分隔符操作数组元素
    print(np.char.join([':', '-'], ['runoob', 'google']))

    print(np.char.replace('i like runoob', 'oo', 'cc'))

    a = np.char.encode('runoob', 'cp500')
    print(a)

    a = np.char.encode('runoob', 'cp500')
    print(a)
    print(np.char.decode(a, 'cp500'))


if __name__ == "__main__":
    # demo_char_add()
    demo_char_1()
