#!/usr/bin/python3
from sys import path

path.append('../')
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")
