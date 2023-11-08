#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    i = None
    j = float('-inf')
    for key, value in a_dictionary.items():
        if value > j:
            i = key
            j = value

    return i
