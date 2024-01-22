#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    print_elements = 0

    for print_elements in range(x):
        try:
            print("{:d}".format(my_list[print_elements]), end="")
            print_elements += 1
        except (TypeError, ValueError):
            print_elements -= 1
    print()
    return print_elements
