#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    len_t_one = len(tuple_a)
    len_t_two = len(tuple_b)
    if len_t_one < 2:
        if len_t_one == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len_t_two < 2:
        if len_t_two == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
