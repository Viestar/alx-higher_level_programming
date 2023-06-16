#!/usr/bin/python3
"""Documentation for from_json_string """


import json


def from_json_string(my_str):
    """ returns an object(python data structure) 

    Args: my_str (JSON string): json string.
    Return: object, the python data structure
    """
    return json.load(my_str)
