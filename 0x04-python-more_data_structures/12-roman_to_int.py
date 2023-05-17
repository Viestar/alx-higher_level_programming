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
        for index in range(str_len):
            if romans.get(roman_string[index], 0) == 0:
                return (0)
            if (index != (str_len - 1) and romans[roman_string[index]] < romans[roman_string[index + 1]]):
                integer = integer + (romans[roman_string[index]] * -1)

            else:
                integer = integer + romans[roman_string[index]]
    else:
        return (0)

    return (integer)
