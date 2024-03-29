#!/usr/bin/python3
"""This module contains add_attribute() function"""


def add_attribute(obj, att_name, att_value):
    """
    Adds a new attribute to an object if it’s possible
    Args:
        obj (object): Is the object to add the new attibute to
        att_name (str): Is the name of the new attribute
        att_value (Any): Is the value of the new attribute

    Raises:
        TypeError: if the object cannot have new attribute
    """

    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, att_name, att_value)
