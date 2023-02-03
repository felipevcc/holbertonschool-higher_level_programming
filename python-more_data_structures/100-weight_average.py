#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    numerator = 0
    denominator = 0
    for ints_tuple in my_list:
        numerator += ints_tuple[0] * ints_tuple[1]
        denominator += ints_tuple[1]
    return numerator / denominator
