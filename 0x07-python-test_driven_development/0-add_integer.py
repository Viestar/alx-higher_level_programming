#!/usr/bin/python3
"""Adding two integers """

def add_integer(a, b=98):
    """ Adds two integerss
    Args:
    a (int): First integer
    b (int): Second integer
    REturns: Sum of the two integers
    """

    if not isinstance(a, (int)):
        raise TypeError("a must be an integer")
    if not isinstance(a, (float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int)):
        raise TypeError("b must be an integer")
    if not isinstance(b, (float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        a = int(b)
    return (a + b)