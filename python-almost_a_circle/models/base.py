#!/usr/bin/python3
"""class Base"""
import json
from os import path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write object to a file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []

        list_dicts = []
        with open(filename, "w") as file:
            for i in list_objs:
                list_dicts.append(i.to_dictionary())
            file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of a JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if not path.exists(filename):
            return []
        with open(filename, "r") as file:
            obj = Base.from_json_string(file.read())
        list = [cls.create(**dict) for dict in obj]
        return list
