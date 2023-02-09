#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """number validation"""
    bool_matrix = [[isinstance(num, (int, float))
                    for num in list] for list in matrix]

    """list length validation"""
    bool_list = [len(matrix[0]) == len(list) for list in matrix]

    """validations"""
    if not all(all(list) for list in bool_matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    elif not all(bool_list):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    """new matrix"""
    new_matrix = [[round(num / div, 2) for num in list] for list in matrix]
    return new_matrix
