#!/usr/bin/python3

""" Class Definition"""


class Square:
	"""Square Class """

	def __init__(self, size=0):
		""" initialisation
		Args:
		size (int): New square size
		"""
		self.size = size

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

    def area(self):
		""" Returns current square area """
        return (self.__size * self.__size)