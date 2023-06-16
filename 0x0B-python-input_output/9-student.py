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

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        return self.__dict__
