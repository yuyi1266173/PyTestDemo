

import cffi


def test_1():
    ffi = cffi.FFI()
    ffi.cdef("""int add(int a, int b);
                int sub(int a, int b);""")

    ffi.set_source('_ext', """ 
        int add(int a, int b) 
        { 
            return a + b; 
        } 
        
        int sub(int a, int b) 
        { 
            return a - b; 
        } """)

    ffi.compile(verbose=True)

    from _ext import lib
    print(lib.add(2, 3))
    print(lib.sub(2, 3))


def test_2():
    ffi = cffi.FFI()
    ffi.cdef("""
    int printf(const char *format, ...);   // copy-pasted from the man page
    """)
    c_fun = ffi.dlopen(None)  # 导入全部C函数命名空间
    arg = ffi.new("char[]", "world")  # 相当于 char arg[] = "world";
    c_fun.printf("hi there, %s.\n", arg)  # 调用 printf


def test_3():
    ffi = cffi.FFI()
    # cdef用来定义结构体,变量,或者方法的声明
    ffi.cdef("""
        typedef struct{
            int x;
            int y;
        } te;
        """)
    t1 = ffi.new("te *", [1, 2])  # 定义一个结构体变量并赋值
    t2 = ffi.new("te *", {'x': 1, 'y': 2})  # 另一种赋值方式
    print(t1.x, t1.y, t2.x, t2.y)


def test_4():
    ffi = cffi.FFI()
    ffi.cdef("""
            int add(int a, int b);
            int sub(int a, int b);
        """)
    # verify是在线api模式的基本方法它里面直接写C代码即可
    lib = ffi.verify("""
            int add(int a,int b){
                return a+b;
            }
            int sub(int a,int b){
                return a-b;
            }""")
    print(lib.add(10, 2))
    print(lib.sub(10, 2))


def test_5():
    ffi = cffi.FFI()
    ffi.cdef("""
        int add(int a, int b);
        void cprint(void);
        int mul(int a,int b);
    """)
    # verify是在线api模式的基本方法它里面直接写C代码即可
    lib = ffi.verify(sources=['test.c'])
    print(lib.add(10, 2))
    lib.cprint()
    print(lib.mul(3, 5))


if __name__ == '__main__':
    # test_1()
    # test_2()
    # test_3()
    # test_4()
    test_5()
