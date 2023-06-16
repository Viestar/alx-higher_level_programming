#!/usr/bin/python3
"""Documentation for pascal_triangle function """


def pascal_triangle(n):
    """ Returns a list of lists of integers representing \
    a pascal triangle

    Args: n (int): number of rows.

    Return: pascal triangle - a list of lists
    """

    if n <= 0:
        return ""

    trianglee = [[1]]
    for row_t in range(1, n):
        row = [1]
        row_p = trianglee[row_t - 1]
        for yxz in range(1, row_t):
            row.append(row_p[yxz] + row_p[yxz - 1])
        row.append(1)
        trianglee.append(row)
    return trianglee
