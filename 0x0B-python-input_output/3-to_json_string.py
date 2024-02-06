#!/usr/bin/python3


"""This module contains to_json_string() function"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string):
    Args:
        my_obj (any): Is the object to return it's JSON representation
    """

    return json.dumps(my_obj)
