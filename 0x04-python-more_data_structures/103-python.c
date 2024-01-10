#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints some basic info about Python lists.
 * @p: Is the list to print its info
 * Return: void
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyObject_GetItem(p, PyLong_FromSsize_t(i));
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints bytes of a Python object.
 * @p: Is the object to print its bytes
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;
	char *string;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	string = PyBytes_AsString(p);
	printf("  trying string: %s\n", string);

	printf("  first %ld bytes: ", (size < 10) ? size : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)string[i]);
	}
	printf("\n");
}
