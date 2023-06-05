#!/usr/bin/python3
"""Rectangle class Definition."""


class Rectangle:
    """Rectangle clss representation."""

    def __init__(self, width=0, height=0):
        """New Rectangle instantition.
        Args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets/sets the Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Checks nd reports errors """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/sets the Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Checks nd reports for errors"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the Rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the Rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
