#!/usr/bin/python3

"""This module contains Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A subclass of the Bass class that represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Is the class constructor"""

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the instance attribute (width)"""
        return self.__width

    @width.setter
    def wdith(self, value):
        """
        Setter for the instance attribute (width)
        Args:
            value: Is the value that will be asigned to width attribute
        """

        self.__width = value

    @property
    def height(self):
        """Getter for the instance attribute (height)"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the instance attribute (height)
        Args:
            value: Is the value that will be asigned to height attribute
        """

        self.__height = value

    @property
    def x(self):
        """Getter for the instance attribute (x)"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the instance attribute (x)
        Args:
            value: Is the value that will be asigned to x attribute
        """

        self.__x = value

    @property
    def y(self):
        """Getter for the instance attribute (y)"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the instance attribute (y)
        Args:
            value: Is the value that will be asigned to y attribute
        """

        self.__y = value
