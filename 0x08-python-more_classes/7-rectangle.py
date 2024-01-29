#!/usr/bin/python3

"""This module Conatins one class (Rectangle)"""


class Rectangle:
    """
    This class represents a rectangle

    Attributes:
        width (int): Is the width of the rectangle
        height (int): Is the height of the rectangle
        number_of_instances (int): The number of instances of Rectangle class
        print_symbol (any): Is the symbol that will represent the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """
        This method initializes the instance

        Args:
            width (int): Is the width of the rectangle
            height (int): Is the height of the rectangle

        raises:
            TypeError: If (width) or (height) is not integer
            ValueError: If (width) or (height) is less than 0
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This method returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method sets the value of width

        Args:
            value (int): Is the value that will be assigned to width

        raises:
            TypeError: If (value) is not an integer
            ValueError: If (value) is less than 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """This method returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method sets the value of height

        Args:
            value (int): Is the value that will be assigned to height

        raises:
            TypeError: If (value) is not an integer
            ValueError: If (value) is less than 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """represents the rectangle with the character (#)"""

        result = []
        if self.__height == 0 or self.__width == 0:
            return ""

        for i in range(self.__height):
            result.append(str(self.print_symbol) * self.__width)
            if i < self.__height - 1:
                result.append("\n")

        return "".join(result)

    def __repr__(self):
        """Returns the canonical string representation of the object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        "Called when the instance is deleted"

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
