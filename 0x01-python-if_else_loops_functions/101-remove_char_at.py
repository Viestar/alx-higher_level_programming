#!/usr/bin/python3
def remove_char_at(str, n):
    counter = 0
    string = ""
    for character in str:
        if counter != n:
            string = string + character
        counter = counter + 1
    return (string)
