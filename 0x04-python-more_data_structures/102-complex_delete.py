#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    try:
        for key in new:
            if value == a_dictionary[key]:
                del a_dictionary[key]
        return (a_dictionary)
    except KeyError:
        return (a_dictionary)
