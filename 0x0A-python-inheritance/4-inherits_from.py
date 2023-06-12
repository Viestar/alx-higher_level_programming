#!/usr/bin/python3
""" Class inheritance checker """


def inherits_from(obj, a_class):
    """ Checks if the obj is a sub class of a_class

    Returns True or False:
    """
    bool = (issubclass(type(obj), a_class) and type(obj) != a_class)
    return (bool)
