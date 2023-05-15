#include <Python.h>

/**
 * print_python_list_info - outputs basic python info
 * @p: Pyproject list
 */

void print_python_list_info(PyObject *p)
{
	PyObject *piece;
	int index;
	int allocate;
	int rrange;

	allocate = ((PyListObject *)p)->allocated;
	rrange = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", rrange);
	printf("[*] Size of the Python List = %d\n", allocate);

	for (index = 0; index < rrange; index++)
	{
		piece = PyList_GetItem(p, index);
		printf("Element %d: ", index);
		printf("%s\n", Py_TYPE(piece))->tp_name;
	}
}