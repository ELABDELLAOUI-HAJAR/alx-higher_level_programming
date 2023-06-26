#include <Python.h>
#include <stdio.h>

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - prints python list
 * @p: the giving object
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	setbuf(stdout, NULL);

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}
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
		if (PyFloat_Check(obj))
			print_python_float(obj);
	}
	setbuf(stdout, NULL);
}

/**
 * print_python_bytes - prints python bytes
 * @p: the giving object
 */
void print_python_bytes(PyObject *p)
{

	long int size, seuil, i;
	char *content;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
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
	setbuf(stdout, NULL);
}

/**
 * print_python_float - prints python float
 * @p: the giving object
 */
void print_python_float(PyObject *p)
{
	double value;
	char *double_str;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	double_str = PyOS_double_to_string(value, 'r', 0,
			Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf("  value: %s\n", double_str);
	setbuf(stdout, NULL);
}
