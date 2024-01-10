#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_nums =\
        {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for index in range(len(roman_string)):
        if index == 0 and roman_string[0] == "I" and roman_string[1] != "I":
            result -= 1
        else:
            result += roman_nums[roman_string[index]]
    return result
