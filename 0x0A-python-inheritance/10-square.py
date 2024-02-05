#!/usr/bin/python3

"""This module contains Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a square"""

    def __init__(self, size):
        """
        The constructor of the class which intitalizes instances
        Args:
            size (int): Is the size of the sqquare
        """
        super().__init__(size, size)
        self.integer_validator("size", size)

        self.__size = size
