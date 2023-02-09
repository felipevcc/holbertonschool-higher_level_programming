#!/usr/bin/python3
"""Function that says my name"""


def say_my_name(first_name, last_name=""):
    """string arguments validation"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
