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
