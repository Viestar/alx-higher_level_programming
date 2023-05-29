#!/usr/bin/python3

def safe_print_division(a, b):
    divisions = 0
    try:
        divisions = a / b
    except (ZeroDivisionError):
        divisions = None
    finally:
        print("Inside result: {}".format(divisions))

    return (divisions)
