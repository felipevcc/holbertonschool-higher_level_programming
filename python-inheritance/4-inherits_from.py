#!/usr/bin/python3
"""Check if an object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Validation"""
    return isinstance(obj, a_class) and type(obj) != a_class
