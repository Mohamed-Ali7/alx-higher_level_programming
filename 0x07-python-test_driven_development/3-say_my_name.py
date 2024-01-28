#!/usr/bin/python3

"""
This mdoule contains (say_my_name) function
which prints the provided first name and last name in a specific way
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints a name in a specific format.

    Args:
        first_name (str): Is the first name to print.
        last_name (str): Is the last name to print.

    Returns:
        My name is <first name> <last name>
    Raises:
        TypeError: if first_name or last_name are not strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
