#!/usr/bin/python3
"""
0-rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """performs in-place 90 degrees clockwise
    rotation of a matrix"""
    size = len(matrix)
    for row in range(size):
        for column in range(size):
            if row < size - 1 and column < size - 1 or row == size - 1:
                swap_buffer = matrix[column][size - 1 - row]
                matrix[column][size - 1 - row] = matrix[row][column]
                matrix[row][column] = swap_buffer
