#!/usr/bin/python3

"""
This module contains addition function that takes
two integer values and return the result of adding these
two integers.
"""


def add_integer(a, b=98):
    """
    This function return the addition result of (a) and (b).

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add., default value is 98.

    Returns:
        The result of adding (a) and (b) as integer value
    Raises:
        TypeError: if (a) or (b) are not int or float.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
