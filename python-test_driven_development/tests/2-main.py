#!/usr/bin/python3
from sys import path

path.append('../')
matrix_divided = __import__('2-matrix_divided').matrix_divided

"""matrix = [
    [1, 2, 3],
    [4, 5, 6]
]"""
matrix = [[1, 2], [3, 4]]
print(matrix_divided(matrix, float('inf')))
print(matrix)
