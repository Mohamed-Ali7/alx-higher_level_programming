#!/usr/bin/python3

"""This module contains addition function"""


def add_integer(a, b=98):
    """This function return the addition result of (a) and (b)"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
