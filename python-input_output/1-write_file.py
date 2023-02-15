#!/usr/bin/python3
"""Write a string to a text file and returns the number of chars written"""


def write_file(filename="", text=""):
    """Write in file"""
    with open(filename, "w", encoding="utf-8") as file:
        num_chars = file.write(text)
    return num_chars
