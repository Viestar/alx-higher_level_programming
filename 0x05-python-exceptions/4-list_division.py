#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    div_result = 0
    div_list = []
    for num in range(0, list_length):

        try:
            div_result = my_list_1[num] / my_list_2[num]

        except ZeroDivisionError:
            div_result = 0
            print("division by 0")
        except TypeError:
            div_result = 0
            print("wrong type")
        except IndexError:
            div_result = 0
            print("out of range")
        finally:
            div_list.append(div_result)

    return (div_list)
