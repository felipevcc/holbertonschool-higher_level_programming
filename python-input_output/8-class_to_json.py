#!/usr/bin/python3
"""Return the dictionary description of an object"""


def class_to_json(obj):
    """Dict description"""
    return obj.__dict__
