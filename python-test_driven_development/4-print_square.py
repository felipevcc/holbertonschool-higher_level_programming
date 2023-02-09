#!/usr/bin/python3
"""Function that prints a square"""


def print_square(size):
    """Type and value validation"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    """generate the square"""
    for row in range(size):
        print("#" * size)
