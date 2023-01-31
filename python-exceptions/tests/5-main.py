#!/usr/bin/python3
from sys import path

path.append('../')
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
