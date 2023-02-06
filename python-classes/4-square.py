#!/usr/bin/python3
"""Class that defines a square by its size"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """
        Args:
            size (int): square size
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Type and value validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
