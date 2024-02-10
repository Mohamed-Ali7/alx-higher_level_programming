#!/usr/bin/python3

"""This module contains Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A subclass of the Bass class that represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Is the class constructor
        Args:
            width (int): The initiation value of the width of the rectangle
            height (int): The initiation value of the height of the rectangle
            x (int): The initiation value of the x of the rectangle
            y (int): The initiation value of the y of the rectangle
            id (int): The initiation value of the id of the rectangle

        Raises:
        TypeError: If width, height, x, or y is not integer
        ValueError: If width or height less that or equal to 0 or
        x or y less than 0
        """

        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the instance attribute (width)"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the instance attribute (width)
        Args:
            value: Is the value that will be asigned to width attribute

        Raises:
        TypeError: If (value) ss not an integer
        ValueError: If (value) is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

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

        Raises:
        TypeError: If (value) ss not an integer
        ValueError: If (value) is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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

        Raises:
        TypeError: If (value) ss not an integer
        ValueError: If (value) is less than 0
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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

        Raises:
        TypeError: If (value) ss not an integer
        ValueError: If (value) is less than 0
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__height * self.__width

    def display(self):
        """Prints the rectangle using (#)"""

        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns new value to each attribute"""

        if args:
            length = len(args) - 1
            self.id = args[0]
            if length > 0 and args[1]:
                self.width = args[1]
                length -= 1
            if length > 0 and args[2]:
                self.height = args[2]
                length -= 1
            if length > 0 and args[3]:
                self.x = args[3]
                length -= 1
            if length > 0 and args[4]:
                self.y = args[4]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Rreturns the dictionary representation of a Rectangle:"""

        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
