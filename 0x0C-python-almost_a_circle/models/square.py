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

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)
