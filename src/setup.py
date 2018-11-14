
from distutils.core import setup, Extension

# // test in master

setup(name='test_dll',
      ext_modules=[
          Extension('test_dll',
                    ['py_test_dll.c'],
                    include_dirs=['.'],
                    define_macros=[('FOO', '1')],
                    undef_macros=['BAR'],
                    library_dirs=['.'],
                    libraries=['test_dll']
                    )
      ])
