#!/usr/bin/python3

def uniq_add(my_list):
    unique = set(my_list)
    summ = 0
    for num in unique:
        summ += num

    return summ
