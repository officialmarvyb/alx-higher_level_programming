#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_add = 0
    for i in set(my_list):
        unique_add += i
    return (unique_add)
