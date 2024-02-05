#!/usr/bin/python3

"""Thid module contains BaseGeometry class"""


class BaseGeometry():
    """This is a base class"""

    def area(self):
        """Raises:
            Exception: if area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value
        Args:
            name (string): Is the name that the (value) will assigned to
            value (int): Is the value that will be assinged to the (name)

        Rasies:
            TypeError: if (value) is not an integer
            ValueError: if (value) is less or equal to 0
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
