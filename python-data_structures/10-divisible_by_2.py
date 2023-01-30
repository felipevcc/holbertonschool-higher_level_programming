#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            check_multiples.append(True)
        else:
            check_multiples.append(False)
    return check_multiples
