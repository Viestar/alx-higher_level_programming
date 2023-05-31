#!/usr/bin/python3

""" Class Definition"""


class Square:
	"""Square Class """

    def __init__(self, size=0):
		""" initialisation
		Args:
		size (int): New square size
		position (int): nEW SUARE position
		"""
        self.size = size
        self.position = position

    @property
    def size(self):
		""" Get/set square current size """
        return (self.__size)

    @size.setter
    def size(self, value):
		""" Raises errors if cannot assign private size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Get/set current position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Reports errors """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(index, int) for index in value) or
                not all(index >= 0 for index in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
       """ Returns the area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ Prints a square with a symbol """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
        if self.__size == 0:
            print()

        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
