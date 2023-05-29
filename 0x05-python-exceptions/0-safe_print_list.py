#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    prinum = 0

    for num in range(x):
        try:
            print(my_list[num], end="")
            prinum += 1
        except IndexError:
            break

    print()
    return (prinum)

    # # length of the list
    # for item in my_list:
    #     list_length += 1

    # # traversing
    # for num in range(x):
    #     if prinum < list_length:
    #         print(my_list[num], end="")
    #         prinum += 1
    # print()

    # return (prinum)
