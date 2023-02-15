#!/usr/bin/python3
"""Append a str at the end of a file and returns the number of chars added"""


def append_write(filename="", text=""):
    """Append str in file"""
    with open(filename, "a", encoding="utf-8") as file:
        num_chars = file.write(text)
    return num_chars
