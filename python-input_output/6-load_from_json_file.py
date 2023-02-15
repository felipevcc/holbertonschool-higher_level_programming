#!/usr/bin/python3
"""Create an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create object"""
    with open(filename, "r") as file:
        obj = json.loads(file.read())
    return obj
