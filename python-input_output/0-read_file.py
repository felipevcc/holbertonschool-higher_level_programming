#!/usr/bin/python3
"""Read a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Read file"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
