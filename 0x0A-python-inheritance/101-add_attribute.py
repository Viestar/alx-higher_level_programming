#!/usr/bin/python3


def add_attribute(obj, name, value):
    """Adds an attribute or raises an error """
    if hasattr(obj, '__dict__'):
        obj.__setattr__(name, value)
    else:
        raise TypeError("Can't add new attribute")
