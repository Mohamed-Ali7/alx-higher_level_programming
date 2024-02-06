#!/usr/bin/python3


"""This module contains save_to_json_file() function"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation:
    Args:
        my_obj (any): Is the object to return it's JSON representation
        filename (str): Is the name of the JSON file to insert JSON value into
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
