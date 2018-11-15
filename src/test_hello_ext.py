
"""
C扩展demo程序
py_test_dll模块引用于 helloext.pyd文件，放在src目录下
helloext.pyd用VS2017 python扩展模块项目生成，项目路径：D:\project\vs_prj\helloext
"""

import helloext

helloext.example("", 2)
