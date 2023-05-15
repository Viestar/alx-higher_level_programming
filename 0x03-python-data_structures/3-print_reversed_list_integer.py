#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for integer in range(length - 1, 0, -1):
        print("{:d}".format(my_list[integer]))
