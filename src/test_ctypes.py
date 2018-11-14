# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2018-11-06
# function: test for ctypes packages

import os
import ctypes
import array
import numpy

# 加载动态库文件
_file = 'test_dll.dll'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file,)))
# print('_path = ', _path)
_mod = ctypes.cdll.LoadLibrary(_path)

# int int Add(int a, int b)
add = _mod.Add
add.argtypes = (ctypes.c_int, ctypes.c_int)
add.restype = ctypes.c_int

# int gcd(int x, int y)
gcd = _mod.gcd
gcd.argtypes = (ctypes.c_int, ctypes.c_int)
gcd.restype = ctypes.c_int

# int in_mandel(double x0, double y0, int n)
in_mandel = _mod.in_mandel
in_mandel.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int)
in_mandel.restype = ctypes.c_int

# 指针 ctypes.POINTER
# int divide(int a, int b, int *remainder)
_divide = _mod.divide
_divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int


def divide(x, y):
    rem = ctypes.c_int()
    quot = _divide(x, y, rem)
    return quot, rem.value


# 封装Double数组类型
class DoubleArrayType:
    def from_param(self, param):
        typename = type(param).__name__
        # print("[DoubleArrayType] typename =", typename)
        if hasattr(self, 'from_' + typename):
            return getattr(self, 'from_' + typename)(param)
        elif isinstance(param, ctypes.Array):
            return param
        else:
            raise TypeError("Can't convert %s" % typename)

    def from_array(self, param):
        if param.typecode != 'd':
            raise TypeError("must be an array of doubles")
        ptr, _ = param.buffer_info()
        return ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double))

    def from_list(self, param):
        val = ((ctypes.c_double)*len(param))(*param)
        return val

    from_tuple = from_list

    def from_ndarray(self, param):
        return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double))


# double avg(double *a, int n);
DoubleArray = DoubleArrayType()
_avg = _mod.avg
_avg.argtypes = (DoubleArray, ctypes.c_int)
_avg.restype = ctypes.c_double


def avg(values):
    return _avg(values, len(values))


# 结构体
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double)]


# double distance(Point *p1, Point *p2);
distance = _mod.distance
distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point))
distance.restype = ctypes.c_double


def test():
    print('add(5, 7) =', add(5, 7))
    print('gcd(24, 7) =', gcd(24, 7))
    print('in_mandel(12.34, 34.23, 3) =', in_mandel(12.34, 34.23, 3))
    print('divide(7, 4) =', divide(7, 4))
    print('avg([3, 2, 7, 8]) =', avg([3, 2, 7, 8]))
    print("avg(array.array('d', [1, 2, 3])) =", avg(array.array('d', [1, 2, 3])))
    print("avg(numpy.array([1.0, 2.0, 3.0])) =", avg(numpy.array([1.0, 2.0, 3.0])))
    p1 = Point(1, 2)
    p2 = Point(4, 5)
    print('distance(p1, p2) =', distance(p1, p2))


if __name__ == "__main__":
    test()
