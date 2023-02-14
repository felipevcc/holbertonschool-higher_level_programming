#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        """Constructor - Initialize a new rectangle"""

        """Type and value validation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description"""
        name = str(self.__class__.__name__)
        w = str(self.__width)
        h = str(self.__height)
        return f"[{name}] {w}/{h}"
