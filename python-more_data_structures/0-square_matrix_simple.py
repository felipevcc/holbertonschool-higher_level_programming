#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = [[num**2 for num in row] for row in matrix]
    return matrix_square
