#!/usr/bin/python3
"""Function Documentation"""


def print_square(size):
    """Prints length with a special character
    Args:
        size (int): Length
    Raises:
        TypeError: incase of non integer
        ValueError: Incase of a negative length.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
