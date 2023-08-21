#!/usr/bin/python3
"""Documenation for the save_to_json function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file.

    Args:
        my_obj (class object): the object.
        filename (file): the storage file.
    """
    with open(filename, "w", encoding='utf-8') as mideh:
        object = json.dumps(my_obj)
        mideh.write(object)
