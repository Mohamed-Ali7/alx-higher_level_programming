#!/usr/bin/python3

"""
This module is to practice classes and objects in Python
just by creating an empty class
"""


class Square:
    """This class represnts a square

    Attributes:
        __size (int): Is a private attribue
        which represents the size of the square
    """

    def __init__(self, size=0):
        """This method initializes the instance

        Args:
            size (int): Is the initializing value of the size attribute
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
