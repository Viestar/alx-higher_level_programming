# 1/usr/bin/python3


def max_integer(my_list=[]):
    len_list = len(my_list)
    big_char = my_list[0]

    if len_list == 0:
        return (None)

    for i in range(len_list):
        if my_list[i] > big_char:
            big_char = my_list[i]

    return (big_char)
