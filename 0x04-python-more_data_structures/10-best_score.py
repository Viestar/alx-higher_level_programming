#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:

        return None

    else:
        num = list(a_dictionary.keys())[0]
        big = a_dictionary[num]

        for ky, val in a_dictionary.items():
            if val > big:
                big = val
                num = ky
        return (num)
