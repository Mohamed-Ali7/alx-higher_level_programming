#!/usr/bin/python3

"""This module contains the find_peak() function"""


def find_peak(list_of_integers):
    """This function finds the peack of a list"""

    if not list_of_integers:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    for i in range(1, len(list_of_integers) - 1):
        next = list_of_integers[i + 1]
        prev = list_of_integers[i - 1]
        if list_of_integers[i] >= prev and list_of_integers[i] >= next:
            return list_of_integers[i]
