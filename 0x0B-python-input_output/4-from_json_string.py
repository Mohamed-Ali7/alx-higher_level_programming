#!/usr/bin/python3


"""This module contains from_json_string() function"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string:
    Args:
        my_obj (any): Is the JSON string to return it's python object
    """

    return json.loads(my_str)
