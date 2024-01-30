#!/usr/bin/python3

"""
This module contains division function (matrix_divided)
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    This function divides all the elements of matrix by a specific number.

    Args:
        matrix (list): A list of lists which it's elements will be divided.

        div (int or float): Is the number that All elements
        of the matrix will be divided by

    Returns:
        A list of lists (matrix) that contains the old matrix
        elements after divided by (div)
    Raises:
        TypeError: if div is not int or float or matrix is not a list of lists\
            or each row of the matrix doesn't have the same size.
        ZeroDivisionError: if div equals 0
    """

    element_err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(element_err)

    new_matrix = [[] for i in range(len(matrix))]

    i = 0
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if type(row) is not list:
            raise TypeError(element_err)

        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(element_err)
            new_matrix[i].append(round(element / div, 2))

        if len(new_matrix[i]) == 0:
            raise TypeError(element_err)

        if len(new_matrix[0]) != len(new_matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        i += 1

    return new_matrix
