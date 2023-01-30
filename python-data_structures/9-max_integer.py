#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = my_list[0]
    for num in my_list:
        if (num > max):
            max = num
    return max
