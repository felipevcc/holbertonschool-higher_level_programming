#!/usr/bin/python3
from sys import path

path.append('../')
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())
