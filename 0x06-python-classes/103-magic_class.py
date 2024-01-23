#!/usr/bin/python3

"""
This module is to practice classes and objects in Python
This module contains Magicclass
"""

import math


class MagicClass:

    """
    This class represnts data that will be compared to a ceratin bytecode
    and these data are area and circumference of a circle

    Attributes:
        __radius (int or float): This attribute represents
        the radius of the circle.
    """
    def __init__(self, radius=0):
        """This method initializes the instance

        Args:
            radius (int or float): Is the initializing value
            of the radius attribute
        """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """This method is to return the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """This method is to return the circumference of the circle"""
        return 2 * math.pi * self.__radius
