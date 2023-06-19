#!/usr/bin/python3
"""Square Module Documentation"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Child class of the Rectangle class
    Grand child of the Base class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation (Creating square Class Objects)
        Args:
            size (int): Square size
            x (int): x coordinate
            y (int): y coordinate
            id (int): Object unique number
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """gets the siz attribute

        Args:
            value (int): Square size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets the siz attribute

        Args:
            value (int): Square size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes 
        Args:
            args (list): list of arguments
            kwargs (dict): Keyword arguments
        """

        if len(args):
            for arg, att in enumerate(args):
                if arg == 0:
                    self.id = att
                elif arg == 1:
                    self.size = att
                elif arg == 2:
                    self.x = att
                elif arg == 3:
                    self.y = att
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns dictionary representation of the quare"""
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return dict

    def __str__(self):
        """overrides the __str__
        Return:
            String representation of the square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)
