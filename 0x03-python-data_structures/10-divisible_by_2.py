#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    mul_list = []
    for num in range(len(my_list)):
        if my_list[num] % 2 != 0:
            mul_list.append(False)
        else:
            mul_list.append(True)

    return (mul_list)
