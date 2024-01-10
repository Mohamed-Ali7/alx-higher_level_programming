#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_numbers = {x for x in my_list}
    result = 0
    for num in uniq_numbers:
        result += num
    return result
