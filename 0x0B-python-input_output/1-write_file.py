#!/usr/bin/python3
"""This module contains write_file() function"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename (str): Is the name of the file to write
        text (str): Is the text that will be written to the file
    """

    with open(filename, "w", encoding="utf-8") as file:
        file_contents = file.write(text)

    return file_contents
