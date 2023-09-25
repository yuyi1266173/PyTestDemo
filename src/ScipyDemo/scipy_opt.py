# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-7-5
# update date: 2023-7-5
# function: demo for study scipy.optimize


from scipy.optimize import root, minimize
from math import cos


def demo_root():
    def eqn(x):
        return x + cos(x)

    myroot = root(eqn, 0)

    print(myroot.x)
    # 查看更多信息
    print(myroot)


def demo_minimize():
    def eqn(x):
        return x ** 2 + x + 2

    mymin = minimize(eqn, 0, method='BFGS')

    print(mymin)


if __name__ == "__main__":
    # demo_root()
    demo_minimize()
