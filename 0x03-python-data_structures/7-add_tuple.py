#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_first = 0
    tuple_a_second = 0
    tuple_b_first = 0
    tuple_b_second = 0
    if len(tuple_a) < 2:
        if len(tuple_a) != 0:
            tuple_a_first = tuple_a[0]
    else:
        tuple_a_first = tuple_a[0]
        tuple_a_second = tuple_a[1]

    if len(tuple_b) < 2:
        if len(tuple_b) != 0:
            tuple_b_first = tuple_b[0]
    else:
        tuple_b_first = tuple_b[0]
        tuple_b_second = tuple_b[1]
    result = (tuple_a_first + tuple_b_first, tuple_a_second + tuple_b_second)
    return result
