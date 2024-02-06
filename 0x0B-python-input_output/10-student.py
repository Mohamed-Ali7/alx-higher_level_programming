#!/usr/bin/python3

"""This module contains Student class"""


class Student:
    """
    This class represents a student
    Attributes:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): The age of the student
    """

    def __init__(self, first_name, last_name, age):
        """The constructor of the class to initialize instances"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""

        my_dict = {}
        if attrs is not None:
            for attribute in attrs:
                if type(attribute) is not str:
                    return self.__dict__

                if attribute in self.__dict__:
                    my_dict[attribute] = self.__dict__[attribute]
            return my_dict

        return self.__dict__
