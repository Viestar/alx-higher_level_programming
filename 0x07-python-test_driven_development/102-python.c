#include <Python.h>

void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p))
    {
        printf("Error: Invalid string object.\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    Py_UCS4 *unicode = PyUnicode_AsUCS4Copy(p);
    if (!unicode)
    {
        printf("Error: Failed to retrieve string data.\n");
        return;
    }

    printf("String: ");
    for (Py_ssize_t i = 0; i < length; i++)
    {
        Py_UCS4 ch = unicode[i];
        printf("%lc", ch);
    }
    printf("\n");

    PyMem_Free(unicode);
}
