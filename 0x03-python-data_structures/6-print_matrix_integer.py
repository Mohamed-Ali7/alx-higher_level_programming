#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        i = 0
        for column in row:
            print("{:d}".format(column), end="")
            if i != len(row) - 1:
                print(" ", end="")
            i += 1
        print()
