#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = sum(num for num in set(my_list))
    return result
