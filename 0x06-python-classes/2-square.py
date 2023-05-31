#!/usr/bin/python3

""" Class Definition"""


class Square:
    """Square Class """

    def __init__(self, size=0):
        """ initialisation
        Args:
        size (int): New square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size <= -1:
            raise ValueError("size must be >= 0")
        self.__size = size
