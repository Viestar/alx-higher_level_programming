#!/usr/bin/python3
"""Rectangle Class Documentation"""


from models.base import Base


class Rectangle(Base):
    """Child class of the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation (Creating Rectangle Class Objects)
        Args:
            width (int): Rectangle width
            height (int): Rectangle height
            x (int): x axis
            y (int): y axis
            id (int): Object unique number.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets/fetches width """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width and reports in case of errors

        Args:
            value (int): Passed value for width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets/fetches height """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height and reports in case of errors

        Args:
            value (int): Passed value for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets/fetches x """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x and reports in case of errors

        Args:
            value (int): Passed value for x
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets/fetches y """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y and reports in case of errors

        Args:
            value (int): Passed value for y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle instance

        Return:
            the area of the current rectangle instance
        """
        return self.__width * self.__height

    def update(self, *args, **kwargs):
        """ Assigns arguments to each attribute """
        if len(args):
            for arg, att in enumerate(args):
                if arg == 0:
                    self.id = att
                elif arg == 1:
                    self.width = att
                elif arg == 2:
                    self.height = att
                elif arg == 3:
                    self.x = att
                elif arg == 4:
                    self.y = att
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns att dictionary of att Rectangle object"""
        rec_dic = {}
        rec_dic["id"] = self.id
        rec_dic["width"] = self.width
        rec_dic["height"] = self.height
        rec_dic["x"] = self.x
        rec_dic["y"] = self.y
        return rec_dic

    def display(self):
        """ Prints the Rectangle in stdout wwith character # """
        for att in range(self.__y):
            print()
        for b in range(self.__height):
            for c in range(self.__x):
                print(' ', end="")
            for d in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """ New representation of the rectangle """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
