#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    
    new_sum = 0
    new_weight = 0

    for score, weight in my_list:
        new_sum += score * weight
        new_weight += weight

    return new_sum / new_weight
