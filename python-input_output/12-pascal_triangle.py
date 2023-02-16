#!/usr/bin/python3
"""Return a matrix of integers representing the Pascal's triangle"""


def pascal_triangle(n):
    """Represents a Pascal's triangle of n"""
    if n <= 0:
        return []

    """Initializes triangle with numbers 1, (x = columns)"""
    triangle = [[1 for x in range(row)] for row in range(1, n + 1)]

    """Pascal triangle"""
    for row in range(2, n):
        for x in range(1, row):
            triangle[row][x] = triangle[row - 1][x] + triangle[row - 1][x - 1]
    return triangle
