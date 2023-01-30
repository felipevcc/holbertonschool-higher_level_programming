#!/usr/bin/python3
def check_tuple(tuple):
    if (len(tuple) == 0):
        tuple = (0, 0)
    elif (len(tuple) == 1):
        tuple = (tuple[0], 0)
    return tuple
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check_tuple(tuple_a)
    tuple_b = check_tuple(tuple_b)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
