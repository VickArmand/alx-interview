#!/usr/bin/python3
"""
0-rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """performs in-place 90 degrees clockwise
    rotation of a matrix"""
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
