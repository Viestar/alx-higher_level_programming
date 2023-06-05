#!/usr/bin/python3
"""Rectangle class Definition."""


class Rectangle:
    """Rectangle class Representation"""

    def __init__(self, width=0, height=0):
        """New Rectangle instantiation.
        Args:
        width (int): The rectangle width.
        height (int): The rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets/sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Checks for errors"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/sets the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Checks nd reports errors"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
