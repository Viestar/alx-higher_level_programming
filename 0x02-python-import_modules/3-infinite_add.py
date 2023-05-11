#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    args = len(sys.argv) - 1
    sum_of_numbers = 0

    for arg in range(1, args + 1):
        sum_of_numbers += int(sys.argv[arg])

    print(sum_of_numbers)
