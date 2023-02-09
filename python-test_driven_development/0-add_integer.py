#!/usr/bin/python3
"""Integers addition"""


def add_integer(a, b=98):
    """
    Args:
        a (int): number 1
        b (int): number 2
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
