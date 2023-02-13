#!/usr/bin/python3
from sys import path

path.append('../')
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())
