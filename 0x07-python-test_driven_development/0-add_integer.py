#!/usr/bin/python3
"""Adding two integers """


def add_integer(a, b=98):
    """ Adds two integerss
    Args:
    a (int): First integer
    b (int, optional): Second integer
    Returns: Sum of the two integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
