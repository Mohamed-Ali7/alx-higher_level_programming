#!/usr/bin/python3

"""This module contains MyInt class"""


class MyInt(int):
    """Custom class that inherits the (int) class"""

    def __init__(self, my_int):
        """Constructor that initializes instances"""

        super().__init__()
        self.my_int = my_int

    def __eq__(self, obj):
        """
        Perform (=) operator in inverted order
        and return true if the two objects are not equal
        """

        return self.my_int != obj

    def __ne__(self, obj):
        """
        Perform (!=) operator in inverted order
        and return true if the two objects are equal
        """

        return self.my_int == obj
