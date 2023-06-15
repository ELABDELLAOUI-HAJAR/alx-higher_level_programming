#include <Python.h>
#include <stdio.h>


/**
 * print_python_bytes - print bytes object info
 * @p: Python object
 */

void print_python_bytes(PyObject *p)
{
	long int size, seuil, i;
	char *content;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	content = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", content);

	if (size >= 10)
		seuil = 10;
	else
		seuil = size + 1;
	printf("  first %ld bytes:", seuil);
	for (i = 0; i < seuil; i++)
		if (content[i] >= 0)
			printf(" %02x", content[i]);
		else
			printf(" %02x", 256 + content[i]);
	printf("\n");
}

/**
 * print_python_list - print Python list info
 * @p: Python object
 */

void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	printf("[*] Python list info\n");
	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
			printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
