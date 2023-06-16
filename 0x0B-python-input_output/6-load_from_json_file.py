#!/usr/bin/python3
""" Documenttion for the load_from_json_file function"""


import json


def load_from_json_file(filename):
    """creates an object from a 'JSON file'

    Args: filename (JSON file): file with strings
    Return: JSON object represented by string in the file
    """

    with open(filename, "r", encoding='utf-8') as mideh:
        jstring = mideh.read()
        object = json.loads(jstring)
        return object
