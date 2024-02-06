#!/usr/bin/python3

"""This module contains class_to_json() function"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary,string, integer and boolean)
    for JSON serialization of an object:

    Args:
        obj (any): The object to return it's description
    """

    return obj.__dict__
