#!/usr/bin/python3
"""Base Class Documentation"""


import json


class Base:
    """Base class Creation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation (Creating Class Objects)
        Args:
            id (int): Unique number for the instance
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
