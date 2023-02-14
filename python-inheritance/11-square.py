#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Constructor - Initialize a new square"""

        """Type and value validation"""
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)
