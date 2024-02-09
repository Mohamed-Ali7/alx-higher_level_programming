#!/usr/bin/python3

"""This module contains Base class"""


class Base:
    """
    This Is the base class for other classes
    Attributes:
    __nb_objects (int): Is the number of objects created from this clase
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor to initialize instances of this class"""

        self.id = 0

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
