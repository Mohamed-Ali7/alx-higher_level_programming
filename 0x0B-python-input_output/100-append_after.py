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

    for i in range(len(file_lines)):
        words = file_lines[i].split()

        for word in words:
            if search_string == word[:len(new_string)]:
                file_lines[i] += f"{new_string}"

    with open(filename, "w", encoding="utf-8") as file:
        file_lines = file.writelines(file_lines)
