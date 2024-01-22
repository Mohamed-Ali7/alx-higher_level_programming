#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
/**
 * print_python_list - Prints some basic info about Python lists.
 * @p: Is the list to print its info
 * Return: void
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = ((PyVarObject *) p)->ob_size;
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item =  PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - Prints bytes of a Python object.
 * @p: Is the object to print its bytes
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	unsigned char *bytes;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (unsigned char *)PyBytes_AsString(p);
	size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyUnicode_AsUTF8AndSize(p, NULL));
	printf("  first %ld bytes:", (size < 10) ? size : 10);
	for (i = 0; i < size && i < 10; ++i)
		printf(" %02x", bytes[i]);

	printf("\n");
}

/**
 * print_python_float - Prints some info about python float.
 * @p: Is the object to print its bytes
 * Return: void
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}
	value = PyFloat_AsDouble(p);
	printf("  value: %f\n", value);
}
