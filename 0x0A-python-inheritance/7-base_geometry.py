#!/usr/bin/python3
"""BaseGeometry class Documentation"""


class BaseGeometry:
    """BaseGeometry class with public methods"""

    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates IF WIDTH AND HEIGHT are integers:
        Args:
        name (str) : name of the value passed
        value (int) : Value of either height and width
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
