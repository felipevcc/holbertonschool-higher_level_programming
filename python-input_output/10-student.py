#!/usr/bin/python3
"""Class that defines a student"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor - Initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dict representation of a instance"""
        dict = self.__dict__
        if attrs is None:
            return dict

        """Retrieves the attributes that are in a list"""
        new_dict = {}
        for attr in dict.keys():
            if attr in attrs:
                new_dict[attr] = dict[attr]
        return new_dict
