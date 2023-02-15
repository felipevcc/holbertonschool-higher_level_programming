#!/usr/bin/python3
"""Return an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """Conversion"""
    return json.loads(my_str)
