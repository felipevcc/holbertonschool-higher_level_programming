#!/usr/bin/python3
"""Class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assignment - Type and value validation"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assignment - Type and value validation"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Assignment - Type and value validation"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Assignment - Type and value validation"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def display(self):
        """Prints rectangle with #"""
        if self.__width <= 0 or self.__height <= 0:
            print()
            return

        symbol = "#"
        print("{}".format("\n" * self.__y), end="")
        for _ in range(self.__height):
            print("{}".format(" " * self.__x), end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attrs = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns the rectangle description"""
        name = str(self.__class__.__name__)
        id = str(self.id)
        w = str(self.__width)
        h = str(self.__height)
        x = str(self.__x)
        y = str(self.__y)
        return f"[{name}] ({id}) {x}/{y} - {w}/{h}"

    def to_dictionary(self):
        """Returns the dict representation of a rectangle"""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
