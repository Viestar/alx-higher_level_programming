#!/usr/bin/python3
"""Documentation for append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """ Appends new_string after the search_string

    Args:
    filename (file): File to be appended
    new_string: string to be added
    search_string: indicates where to insert
    Return: new file

    """

    with open(filename, "r+", encoding='utf-8') as mideh:

        for current_string in mideh:
            if search_string in current_string:
                mideh.write(new_string)
            else:
                continue
    return mideh
