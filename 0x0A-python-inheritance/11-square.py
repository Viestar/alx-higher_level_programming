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

    def area(self):
        """Calculates rectangle area and returns it"""
        area = self.__width * self.__height

        return area

    def __str__(self):
        """ Special method for ouput formating

        Return:
            Formatted representation of the rectangle.
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Class inherits from parent and the grand parent """

    def __init__(self, size):
        """Square instantiation"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Square area is calculated using this method
        Return:
            area of the square
        """
        area = self.__size ** 2
        return area

    def __str__(self):
        """Presents an output in the required format.
        Return:
            Square representation.
        """
        square = ("[Square] {}/{}".format(self.__size, self.__size))
        return square
