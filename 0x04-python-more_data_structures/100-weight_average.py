#!/usr/bin/python3
def weight_average(my_list=[]):
    nums = 0
    average = 0

    for part in my_list:
        nums += (part[0] * part[1])
        average += part[1]
    return nums / average
