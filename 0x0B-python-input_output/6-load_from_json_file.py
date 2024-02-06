#!/usr/bin/python3


"""This module contains load_from_json_file() function"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file
    Args:
        filename (str): Is the name of the JSON file
    """

    with open(filename, "r") as file:
        obj = json.load(file)

    return obj
