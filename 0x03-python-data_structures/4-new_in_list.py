#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx >= 0 or idx < len(my_list):
        list_copy = [i for i in my_list]
        list_copy[idx] = element
        return list_copy
    return my_list
