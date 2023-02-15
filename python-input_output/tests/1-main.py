#!/usr/bin/python3
from sys import path

path.append('../')
write_file = __import__('1-write_file').write_file

nb_characters = write_file("1-file.txt", "This School is so cool!\n")
print(nb_characters)
