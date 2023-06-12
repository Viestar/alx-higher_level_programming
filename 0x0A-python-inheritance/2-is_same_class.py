#!/usr/bin/python3
"""Class checker Documentation"""


def is_same_class(obj, a_class):
    """ Checks if the obj is a sub class of a_class

    Returns True or False:
    """
    bool = (type(obj) == a_class)
    return (bool)
