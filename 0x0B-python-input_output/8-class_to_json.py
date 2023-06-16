#!/usr/bin/python3
"""Documentation for the class_to_json function"""


def class_to_json(obj):
    """returns a dictionary representation of a python object"""

    return obj.__dict__
