#!/usr/bin/python3

"""
This mdoule contains (matrix_mul) function
which multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    This function return multiplies 2 matrices

    Args:
        m_a (list): Is the first matrix (list of lists)
        m_b (list): Is the second matrix (list of lists)

    Raises:
        ValueError: If m_a and m_b cannot be multiplied
        TypeError: If m_a or m_b is not a list of lists
        or if one element of those list of lists is not an integer or a float
        or if m_a or m_b is not a rectangle (all rows have the same size)
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not m_a:
        raise ValueError("m_a can't be empty")
    for m in m_a:
        if not m:
            raise ValueError("m_a can't be empty")

    if not m_b:
        raise ValueError("m_b can't be empty")
    for m in m_b:
        if not m:
            raise ValueError("m_b can't be empty")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    for i in range(len(m_a)):
        if len(m_a[0]) != len(m_a[i]):
            raise TypeError("each row of m_a must be of the same size")

    for i in range(len(m_b)):
        if len(m_b[0]) != len(m_b[i]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[] for i in range(len(m_a))]

    x = 0

    for row in m_a:
        for s in range(len(m_b[0])):
            element = 0
            for i in range(len(m_b)):
                element += row[i] * m_b[i][s]
            result[x].append(element)
        x += 1
    return result
