#!/usr/bin/python3

"""This module contains read_file() function"""


def read_file(filename=""):
    """R
    eads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): Is the name of the file to read
    """

    with open(filename, "r", encoding="utf-8") as file:
        file_content = file.read()
    print(file_content, end="")
