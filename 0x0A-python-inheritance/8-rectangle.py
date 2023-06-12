#!/usr/bin/python3
"""BaseGeometry class Documentation"""


class BaseGeometry:
    """BaseGeometry class with public methods"""

    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates IF WIDTH AND HEIGHT are integers"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))


class Rectangle(BaseGeometry):
    """An instance of the BaseGeometry class """

    def __init__(self, width, height):
        """Adding special features for the class.
        Args:
            width (int) : Rectangle width.
            height (int): Rectangle height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
