#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    """Public class attributes"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor - Initialize a new rectangle
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Type and value validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Type and value validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __repr__(self):
        """Returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        w = str(self.__width)
        h = str(self.__height)
        return "Rectangle(" + w + ", " + h + ")"

    def __str__(self):
        """Prints the rectangle"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += "\n"
        return rect

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""

        """Type validation"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        """Returns the biggest"""
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance as a square"""
        return cls(size, size)

    def __del__(self):
        """Prints a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
