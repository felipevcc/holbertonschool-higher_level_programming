#!/usr/bin/python3
class Square:
    # Class that defines a square by its size
    def __init__(self, size=0):
        # Type and value validation
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        # Returns the current square area
        return self.__size ** 2
