#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size <= -1:
            raise ValueError("size must be >= 0")
