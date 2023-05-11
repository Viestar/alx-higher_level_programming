#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import div, sub, add, mul
    import sys

    args = len(sys.argv)

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    signs = {
        "+": add,
        "-": sub,
        "/": div,
        "*": mul
    }

    if sys.argv[2] not in list(signs.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, sys.argv[2], b, signs[sys.argv[2]](a, b)))
