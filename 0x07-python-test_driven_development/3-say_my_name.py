#!/usr/bin/python3
"""Function Documentation"""


def say_my_name(first_name, last_name=""):
    """Prints both names.
    Args:
        first_name (str): the first name
        last_name (str, optional): the last name
    Raises:
        TypeError: incase no strings are passed
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
