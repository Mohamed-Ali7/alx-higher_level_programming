#!/usr/bin/python3

"""This module contains Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle"""

    def __init__(self, width, height):
        """
        The constructor of the class which intitalizes instances
        Args:
            width (int): Is the width of the rectanglge
            height (int): IS the height of the rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
