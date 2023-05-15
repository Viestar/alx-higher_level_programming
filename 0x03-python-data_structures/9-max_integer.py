#!/usr/bin/python3


def max_integer(my_list=[]):
    len_list = len(my_list)
    big_char = my_list[0]

    if len_list == 0:
        return (None)

    for x in range(len_list):
        if my_list[x] > big_char:
            big_char = my_list[x]

    return (big_char)
