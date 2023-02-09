#!/usr/bin/python3
from sys import path

path.append('../')
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name("h", 12)
except Exception as e:
    print(e)
