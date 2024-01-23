#!/usr/bin/python3

"""
This module is to practice classes and objects in Python
This module contains a Square class which represnts a square
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
        if type(size) is not int and type(size) is not float:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """This method return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the value of the size of the square
        Args:
            value (int): Is the value to assign to the size of the square
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method is to return the area of the square"""
        return self.__size ** 2

    def __eq__(self, value):
        if isinstance(value, Square):
            if (self.area() == value.area()):
                return True
        return False

    def __nq__(self, value):
        if isinstance(value, Square):
            if (self.area() == value.area()):
                return False
        return True

    def __lt__(self, value):
        return self.area() < value.area()

    def __le__(self, value):
        return self.area() < value.area() or self.area() == value.area()

    def __gt__(self, value):
        return self.area() > value.area()

    def __ge__(self, value):
        return self.area() > value.area() or self.area() == value.area()
