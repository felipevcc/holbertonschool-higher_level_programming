#!/usr/bin/python3
"""Class that inherits"""


class MyList(list):
    """prints sorted list"""
    def print_sorted(self):
        print(sorted(self))
