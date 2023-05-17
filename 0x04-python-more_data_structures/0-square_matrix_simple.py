#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return ([list(map(lambda s: s * s, r)) for r in matrix])
