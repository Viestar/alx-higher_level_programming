#!/usr/bin/python3
"""Documentation for json_string function"""


import json


def to_json_string(my_obj):
    """Creates a Json object.

    Args: my_obj (class object): the object to convert to a JSON string
    Return: Json respresentation
    """
    return json.dumps(my_obj)
