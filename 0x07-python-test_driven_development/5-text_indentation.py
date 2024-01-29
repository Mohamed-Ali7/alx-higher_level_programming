#!/usr/bin/python3

"""
This mdoule contains (text_indentation) function
which prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This method prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): Is the text to print.

    Raises:
        TypeError: if (text) is not str
    """

    new_text = []
    if type(text) is not str:
        raise TypeError("text must be a string")

    for chr in text:
        if new_text and (new_text[-1] == "\n\n" or new_text[-1] == "\n")\
                    and chr == " ":
            continue
        new_text.append(chr)
        if chr in [".", "?", ":"]:
            new_text.append("\n\n")

    print("".join(new_text), end="")
