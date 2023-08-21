#!/usr/bin/python3
"""Documentation for read file function """


def read_file(filename=""):
    """Reads and prints a file to the standard output"""

    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end="")
