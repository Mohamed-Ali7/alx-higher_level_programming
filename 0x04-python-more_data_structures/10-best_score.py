#!/usr/bin/python3
def best_score(a_dictionary: dict):

    result = ""
    score = 0
    if not a_dictionary:
        return None

    for key, value in a_dictionary.items():
        if score < value:
            score = value
            result = key
    return result
