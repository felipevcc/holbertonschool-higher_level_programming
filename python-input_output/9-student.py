#!/usr/bin/python3
"""Class that defines a student"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor - Initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dict representation of a instance"""
        return self.__dict__
