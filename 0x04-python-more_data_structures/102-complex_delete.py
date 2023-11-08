#!/usr/bin/python3
def complex_delete(a_dictionary, value):
   del_ keys = [key for key in a_dictionary if a_dictionary[key] == value]
    for key in del_keys:
        a_dictionary.pop(key, None)
    return a_dictionary
