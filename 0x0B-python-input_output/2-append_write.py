#!/usr/bin/python3
"""This module contains append_write() function"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename (str): Is the name of the file to append to
        text (str): Is the text that will be appended to the file
    """

    with open(filename, "a", encoding="utf-8") as file:
        file_contents = file.write(text)

    return file_contents
