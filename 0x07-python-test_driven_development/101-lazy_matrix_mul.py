#!/usr/bin/python3
""" LAzy matrix Documentation"""
import numpy as num


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies two matrices using numpy module """
    matrix_one = num.array(m_a)
    matrix_two = num.array(m_b)

    product = num.dot(matrix_one, matrix_two).reshape(-1, 1)

    return product.tolist()
