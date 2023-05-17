#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - outputs list info
 * @p: list object
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *object = (PyListObject *)p;
	Py_ssize_t index = 0;
	Py_ssize_t size;

	size = object->ob_base.ob_size;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", object->allocated);

	for (; index < size; index++)
	{
		printf("Element %ld: %s\n", index, object->ob_item[index]->ob_type->tp_name);
	}
}