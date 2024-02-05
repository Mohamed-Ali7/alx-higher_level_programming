#!/usr/bin/python3

def add_attribute(obj, att_name, att_value):
    """
    Adds a new attribute to an object if it’s possible
    Args:
        obj (Any): Is the object to add the new attibute to
        att_name (str): Is the name of the new attribute
        att_value (Any): Is the value of the new attribute

    Raises:
        TypeError: if the object cannot have new attribute
    """

    setattr(obj, att_name, att_value)

    if not hasattr(obj, att_name):
        raise TypeError("can't add new attribute")
