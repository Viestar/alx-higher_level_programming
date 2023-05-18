#!/usr/bin/python3

def roman_to_int(roman_string):
    integer = 0
    str_len = len(roman_string)
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    if (isinstance(roman_string, str) or roman_string is not None):
        for index, rom in enumerate(roman_string):
            if index != 0 and romans.get(rom) > romans.get(roman_string[index - 1]):
                integer = integer + (romans.get(rom) - 2 *
                                     romans.get(rom[index - 1]))

            else:
                integer = integer + romans.get(rom)
    else:
        return (0)

    return (integer)
