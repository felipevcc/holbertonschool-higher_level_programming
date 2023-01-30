#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            my_list[i] = True
        else:
            my_list[i] = False
    return my_list
