#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    run_average = 0
    size = 0

    if isinstance(my_list, list) or len(my_list > 0):
        for num in my_list:
            run_average += (num[0] * num[1])
            size += num[1]
        average = (run_average / size)
        return (average)

    else:
        return (0)
