#!/usr/bin/python3
"""This mdoule conatins LockedClass class"""


class LockedClass:
    """
    This class prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.
    """

    def __setattr__(self, name, value):
        error = f"'{__class__.__name__}' object has no attribute '{name}'"
        if name != "first_name":
            raise AttributeError(error)
        self.__dict__[name] = value
