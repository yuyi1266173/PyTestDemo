
"""
C扩展demo程序
py_test_dll模块引用于py_test_dll.pyd文件，放在src目录下
helloext.pyd用VS2017 python扩展模块项目生成，项目路径：D:\project\vs_prj\py_test_dll
"""

import py_test_dll

print(py_test_dll.Add(3, 5))
print(py_test_dll.gcd(35, 42))
print(py_test_dll.in_mandel(0, 0, 500), py_test_dll.in_mandel(2.0, 1.0, 500))
print(py_test_dll.divide(42, 8))
