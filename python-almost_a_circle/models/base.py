#!/usr/bin/python3
"""class Base"""


class Base:
    """Represents the base model"""

    """Public class attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
