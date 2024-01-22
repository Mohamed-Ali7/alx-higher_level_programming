#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    print_elements = 0

    try:
        for element in my_list:
            print(element, end="")
            print_elements += 1
    except IndexError:
        pass
    print()
    return print_elements
