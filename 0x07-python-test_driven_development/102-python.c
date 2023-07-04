#include <Python.h>
#include <stdio.h>

/**
 * print_python_string -  prints Python strings
 * @p: the giving object
 */

void print_python_string(PyObject *p)
{
	long int len;

	setbuf(stdout, NULL);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	len = ((PyASCIIObject *)(p))->length;

	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));

}
