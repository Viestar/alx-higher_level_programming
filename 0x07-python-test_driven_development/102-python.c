#include <Python.h>

void print_python_string(PyObject *p)
{
    /* Check if a string is valid */
    if (!PyUnicode_Check(p))
    {
        printf("Usage: Invalid string.\n");
        return;
    }
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    Py_UCS4 *unicode = PyUnicaode_AsUCS4Copy(p);

    if (!unicode)
    {
        printf("Error: Failed to retrieve string data\n");
        return;
    }
    printf("String: ") for (Py_ssize_t i = 0; i < length; i++)
    {
        Py_UCS4 chaar = unicode[i];
        printf("%lc", chaar);
    }
    printf("\n");

    PyMem_Free(unicode);
}
