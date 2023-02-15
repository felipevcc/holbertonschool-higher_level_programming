#!/usr/bin/python3
"""Write an object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write object in file"""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
