#!/usr/bin/python3
"""Documentation for class Student """


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """instantiaton function for the class Student

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student.

        Args:
            attrs (python objects): objects to be retunerd

        """
        if not isinstance(attrs, list):
            return self.__dict__
        for attribute in attrs:
            if not isinstance(attribute, str):
                return self.__dict__
        new_dictionary = {}
        for str_att in attrs:
            if str_att in self.__dict__.keys():
                new_dictionary[str_att] = self.__dict__[str_att]
        return new_dictionary

    def reload_from_json(self, json):
        """replaces all attributes of the student"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
