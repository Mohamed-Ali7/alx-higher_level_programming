#!/usr/bin/python3

"""This module contains Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass of the Rectangle class that represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Is the class constructor
        Args:
            size (int): The initiation value of the size of the square
            x (int): The initiation value of the x of the square
            y (int): The initiation value of the y of the square
            id (int): The initiation value of the id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""

        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square
        Args:
            value (int): Is the value to assign to the size of the square
        """

        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the square"""

        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)
