#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    prinum = 0

    for num in range(0, x):
        try:
            print("{:d}".format(my_list[num]), end="")
            prinum += 1
        except (ValueError, TypeError):  # IndexError?
            continue
    print()
    return (prinum)
