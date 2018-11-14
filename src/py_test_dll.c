
#include "Python.h"
#include "test_dll.h"

//int Add(int a, int b)
static PyObject *py_Add(PyObject *self, PyObject *args)
{
    int a, b, res;

    if(!PyArg_ParseTuple(args, "ii", &a, &b))
    {
        return NULL;
    }

    res = Add(a, b);

    return Py_BuildValue("i", res);
}


//int gcd(int x, int y)
static PyObject *py_gcd(PyObject *self, PyObject *args)
{
    int x, y, res;

    if(!PyArg_ParseTuple(args, "ii", &x, &y))
    {
        return NULL;
    }

    res = gcd(x, y);

    return Py_BuildValue("i", res);
}


//int in_mandel(double x0, double y0, int n)
static PyObject *py_in_mandel(PyObject *self, PyObject *args)
{
    double x0, y0;
    int n;
    int res;

    if(!PyArg_ParseTuple(args, "ddi", &x0, &y0, &n))
    {
        return NULL;
    }

    res = in_mandel(x, y, n);

    return Py_BuildValue("i", res);
}


//int divide(int a, int b, int *remainder)
static PyObject *py_divide(PyObject *self, PyObject *args)
{
    int a, b, qout, remainder;

    if(!PyArg_ParseTuple(args, "ii", &a, &b))
    {
        return NULL;
    }

    qout = divide(a, b, &remainder);

    return Py_BuildValue("(ii)", qout, remainder);
}


//Module method table
static PyMethodDef test_dll_methods[] = {
    {"Add", py_Add, METH_VARARGS, "test Add function"},
    {"gcd", py_gcd, METH_VARARGS, "test gcd function"},
    {"in_mandel", py_in_mandel, METH_VARARGS, "test in_mandel function"},
    {"divide", py_divide, METH_VARARGS, "test divide function"},
    {NULL, NULL, 0, NULL}
};


//Module structure
static struct PyModuleDef test_dll_module = {
    PyModuleDef_HEAD_INIT,
    "test_dll",
    "test dll module",
    -1,
    test_dll_methods
};


//Module initialization function
PyMODINIT_FUNC
PyInit_test_dll(void){
    return PyModule_Create(&test_dll_module)
}

