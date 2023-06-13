#!/usr/bin/python3
"""Documentation for append_write """


def append_write(filename="", text=""):
    """ Appends a file

    Args: text (str): a string.
    Return: Number of characters added.
    """

    with open(filename, "a", encoding='utf-8') as mideh:
        return mideh.write(text)
