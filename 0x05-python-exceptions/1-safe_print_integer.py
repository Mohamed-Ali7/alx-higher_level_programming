#!/usr/bin/python3

def safe_print_integer(value):

    print_elements = 0

    try:
        print("{:d}".format(value))
    except TypeError:
        return False
    return True
