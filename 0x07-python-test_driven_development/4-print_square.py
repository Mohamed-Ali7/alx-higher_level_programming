#!/usr/bin/python3

"""
This mdoule contains (print_square) function
which prints a square with the character #.
"""


def print_square(size):
    """
    This method prints the square (n) times where n is the size

    Args:
        size (int): Is the length of the square.

    Raises:
        TypeError: if size is not int or size is float and less than 0
        ValueError: if size is int and less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
