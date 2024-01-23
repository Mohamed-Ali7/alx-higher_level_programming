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

    def __init__(self, size=0, position=(0, 0)):

        """This method initializes the instance

        Args:
            size (int): Is the initializing value of the size attribute
            position (tuple): a tuple of 2 positive integers
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) is not tuple or len(position) != 2 or\
                position[0] < 0 or position[1] < 0:
            print("position must be a tuple of 2 positive integers")

        self.__position = position

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

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method is to return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        """This method return the value of the position attribute"""

        return self.__position

    @position.setter
    def position(self, value):
        """This method sets the value of the position attribute
        Args:
            value (int): Is the value to assign to the position attribute
        """

        if type(value) is not tuple or len(value) != 2 or\
                value[0] < 0 or value[1] < 0:
            print("position must be a tuple of 2 positive integers")

        self.__position = value
