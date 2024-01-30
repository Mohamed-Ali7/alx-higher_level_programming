#!/usr/bin/python3

"""
This mdoule contains (lazy_matrix_mul) function
which multiplies 2 matrices
"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    This function return multiplies 2 matrices

    Args:
        m_a (list): Is the first matrix (list of lists)
        m_b (list): Is the second matrix (list of lists)
    """
    return numpy.matmul(m_a, m_b)
