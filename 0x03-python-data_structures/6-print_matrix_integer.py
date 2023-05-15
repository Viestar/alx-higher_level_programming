#!/usr/bin/python3
"""
def print_matrix_integer(matrix=[[]]):
    for a in range(len(matrix)):
        for b in range(len(matrix)[a]):
            print("{:d}".format(matrix[a][b]), end="")
            if b == len(matrix) - 1:
                pass
            else:
                print(" ", end="")
        print("")
"""


def print_matrix_integer(matrix=[[]]):
    len_matrix = len(matrix)
    for a in range(len_matrix):
        for b in range(len(matrix[a])):
            print("{:d}".format(matrix[a][b]), end="")
            if b != (len(matrix[a]) - 1):
                print(" ", end="")

        print("")
