#!/usr/bin/python3

"""This module contains append_after() function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str): Is the name of the file to insert to
        search_string (str): IS the string to insert after
        new_string (str): Is the new string to insert to the file
    """

    with open(filename, "r", encoding="utf-8") as file:
        file_lines = file.readlines()

    new_lines = []

    r = 0
    for line in file_lines:
        new_lines.append(line)
        r += 1
        if line.find(search_string) >= 0:
            new_lines.append(new_string)
            r += 1

    with open(filename, "w", encoding="utf-8") as file:
        file_lines = file.writelines(new_lines)
