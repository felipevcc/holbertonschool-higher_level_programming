#!/usr/bin/python3
"""Integers addition"""


def add_integer(a, b=98):
    """
    Args:
        a (int): number 1
        b (int): number 2
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
