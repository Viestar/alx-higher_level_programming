#!/usr/bin/python3
"""Function Documentation"""


def text_indentation(text):
    """Splits a string
    Args:
        text (str): The string
    Raises:
        TypeError: Incase of non-string argument.
    """
    indicator = 0

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for character in text:
        if indicator == 1:
            if character == ' ':
                continue
            else:
                indicator = 2
        if indicator == 2:
            if character == '?' or character == '.' or character == ':':
                print(character)
                print()
                indicator = 1
            else:
                print(character, end="")
