#!/usr/bin/python3
"""Base Class Documentation"""


import json


class Base:
    """Base class Creation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation (Creating Base Class Objects)
        Args:
            id (int): Unique number for the instance
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string of a list of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances which inherits from Base
        """
        filename = cls.__name__ + ".json"
        list_objects = []
        if list_objs is not None:
            for x in list_objs:
                list_objects.append(cls.to_dictionary(x))
        with open(filename, 'w', encoding='utf-8') as myFile:
            myFile.write(cls.to_json_string(list_objects))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set

        Args:
            dictionary (dict): Attributes to set
        Return:
            the instance with all the attributes set
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns instances list from a file with JSON object

        Return:
            the instance list object with all instances initialized
        """
        filename = cls.__name__ + ".json"
        json_from_list = []
        try:
            with open(filename, 'r', encoding='utf-8') as myFile:
                json_from_list = cls.from_json_string(myFile.read())
            for x, y in enumerate(json_from_list):
                json_from_list[x] = cls.create(**json_from_list[x])
        except:
            pass
        return json_from_list
