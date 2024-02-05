#!/usr/bin/python3

"""This module contains inherits_from() functions"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    """

    return isinstance(obj, a_class)
