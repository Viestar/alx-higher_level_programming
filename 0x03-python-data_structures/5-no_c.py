#!/usr/bin/python3

def no_c(my_string):
    string_copy = [i for i in my_string if i != 'C' or i != 'c']
    return ("".join(string_copy))
