#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_list = []
    square_matrix = []
    for row in matrix:
        square_list = list(map(lambda x: x ** 2, row))
        square_matrix.append(square_list)
    return square_matrix
