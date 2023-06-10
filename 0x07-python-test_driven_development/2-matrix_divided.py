#!/usr/bin/python3
"""Matrix Division Documentation """


def matrix_divided(matrix, div):
    """Divides a matrix by either an integer or a float

    Args:
    matrix (list): MAtrix
    div (int, float): Integer of flaot
    Returns: Resultant matrix
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
                   
    if len(matrix) == 0 or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for index in matrix:
        if len(index) == 0:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

        if not isinstance(index, list):
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    size = None
    for length in matrix:
        if size is None:
            size = len(length)
        if size != len(length):
            raise TypeError("Each row of the matrix must have the same size")
        for index in range(len(matrix)):
            for len_2 in range(len(matrix[index])):
                if not isinstance(matrix[index][len_2], (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        new_matrix = []
        for index in matrix:
            new_matrix.append(list(map(lambda x: round(x / div, 2), index)))
        return new_matrix
