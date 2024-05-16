#!/usr/bin/python3
"""
This module has a function that solves N queens problem
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard
"""


def nqueens(n):
    """
    N must be an integer greater or equal to 4
    """
    try:
        n = int(n)
    except ValueError:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)


if __name__ == '__main__':
    import sys
    n = sys.argv[1]
    nqueens(n)
