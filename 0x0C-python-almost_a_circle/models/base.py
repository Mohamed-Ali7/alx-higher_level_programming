#!/usr/bin/python3

"""This module contains Base class"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list of dictionaries
        Args:
            list_dictionaries (list of dicts): The list of dictionaries
            to return it's own JSON string representation
        """

        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): A list of instances who inherits of Base
            for example: list of Rectangle or list of Square instances
        """

        file_name = f"{cls.__name__}.json"
        with open(file_name, "w", encoding="utf-8") as file:

            if list_objs:
                list_objs = [obj.to_dictionary() for obj in list_objs]

            list_objs_to_json = cls.to_json_string(list_objs)
            file.write(list_objs_to_json)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        Args:
            json_string (str): s a string representing a list of dictionaries
        """

        if not json_string:
            return []

        return json.loads(json_string)
