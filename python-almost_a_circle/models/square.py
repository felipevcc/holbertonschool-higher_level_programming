#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the rectangle description"""
        name = str(self.__class__.__name__)
        id = str(self.id)
        size = str(self.width)
        x = str(self.x)
        y = str(self.y)
        return f"[{name}] ({id}) {x}/{y} - {size}"

    @property
    def size(self):
        """Retrieves size"""
        return self.width

    @size.setter
    def size(self, value):
        """Assignment - Type and value validation"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attrs = ["id", "size", "x", "y"]
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dict representation of a square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
