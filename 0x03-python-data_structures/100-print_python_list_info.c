#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to Python Object
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *p_list = (PyListObject *)p;
	PyObject *item;
	Py_ssize_t size = PyList_Size(p), i = 0;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", p_list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
