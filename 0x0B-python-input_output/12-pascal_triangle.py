#!/usr/bin/python3

"""This module contains pascal_triangle() function"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    Args:
        n (int): Is the length of the pascal's triangle
    """

    my_list = []

    if n <= 0:
        return my_list

    my_list = [[] for i in range(n)]
    my_list[0].append(1)

    for i in range(1, n):
        for r in range(i + 1):
            if r == 0 or r == i:
                my_list[i].append(1)
            else:
                x = my_list[i - 1][r] + my_list[i - 1][r - 1]
                my_list[i].append(x)

    return my_list
