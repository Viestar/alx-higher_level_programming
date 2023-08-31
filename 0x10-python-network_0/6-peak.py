#!/usr/bin/python3
""" Peak integer identifier """


def find_peak(list_of_integers):
    """ Find the peak integer of an un sorted list """
    local_list = list_of_integers
    local_list.sort()
    if local_list:
        return local_list[-1]
    else:
        return None
