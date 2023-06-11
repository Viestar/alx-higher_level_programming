#!/usr/bin/python3
"""Maximum Integer finder """


def max_integer(list=[]):
    """Returns maximum interger or None """
    if len(list) == 0:
        return None

    index = 1
    
    max_number = list[0]
    while index < len(list):
        if list[index] > max_number:
            max_number = list[index]
        index += 1
    return max_number
