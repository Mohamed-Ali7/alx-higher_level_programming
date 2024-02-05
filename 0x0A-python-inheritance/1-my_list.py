#!/usr/bin/python3

"""Thid module contains MyList class"""


class MyList(list):
    """This is a custom class that inherits (list) class """

    def print_sorted(self):
        print(sorted(self))
