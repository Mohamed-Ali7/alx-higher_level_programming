#include <Python.h>

/**
 * print_python_string - Prints Python strings.
 * @p: Is the Python string to print
 * Return: void
*/
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	Py_ssize_t i;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n", PyUnicode_AsUnicode(p));
}
