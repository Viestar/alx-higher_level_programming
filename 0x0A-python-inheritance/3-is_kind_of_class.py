#!/usr/bin/python3
"""Class checker documentation"""


def is_kind_of_class(obj, a_class):
    """ Checks if the obj is a sub class of a_class

    Returns True or False:
    """
    bool = (isinstance(obj, a_class))
    return (bool)
