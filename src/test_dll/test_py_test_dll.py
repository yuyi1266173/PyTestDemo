
"""
C扩展demo程序
py_test_dll模块引用于py_test_dll.pyd文件，放在src目录下
helloext.pyd用VS2017 python扩展模块项目生成，项目路径：D:\project\vs_prj\py_test_dll
"""

import array
import numpy
import py_test_dll


def test():
    print(py_test_dll.Add(3, 5))
    print(py_test_dll.gcd(35, 42))
    print(py_test_dll.in_mandel(0, 0, 500), py_test_dll.in_mandel(2.0, 1.0, 500))
    print(py_test_dll.divide(42, 8))

    # 数组
    print(py_test_dll.avg(array.array('d', [1, 2, 3])), py_test_dll.avg(numpy.array([1., 2., 3.])))

    # TypeError: a bytes-like object is required, not 'list'
    # print(py_test_dll.avg([1, 2, 3]))

    # TypeError: a bytes-like object is required, not 'str'
    # print(py_test_dll.avg('hello world'))

    p1 = py_test_dll.Point(2, 3)
    p2 = py_test_dll.Point(4, 5)
    print(p1, p2, py_test_dll.distance(p1, p2))


if __name__ == "__main__":
    test()
