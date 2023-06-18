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
