#!/usr/bin/python3
"""Documentation for write file function"""


def write_file(filename="", text=""):
    """ String Writer

    Args:
        text (str): string
    Return:
        written number of characters.
    """

    with open(filename, "w", encoding='utf-8') as mideh:
        return mideh.write(text)
