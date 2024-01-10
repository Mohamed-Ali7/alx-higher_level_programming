#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_nums =\
        {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev_result = 0
    for roman in roman_string:
        if prev_result < roman_nums[roman]:
            result -= prev_result * 2
        result += roman_nums[roman]
        prev_result = roman_nums[roman]
    return result
