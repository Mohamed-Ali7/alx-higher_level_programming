#!/usr/bin/python3

"""This module contains the find_peak() function"""


def find_peak(list_of_integers):
    """This function finds the peack of a list"""

    if not list_of_integers:
        return None

    peak = list_of_integers[0]

    start = 0
    end = len(list_of_integers) - 1

    while (start < end):
        if list_of_integers[start] > peak:
            peak = list_of_integers[start]

        if list_of_integers[end] > peak:
            peak = list_of_integers[end]

        start += 1
        end -= 1

    return peak
