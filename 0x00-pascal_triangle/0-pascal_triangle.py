"""
This module contains a function called
pascal_triangle
"""


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    result = []
    if (n <= 0):
        return result
    for i in range(n):
        if i == 0:
            result.append([1])
        elif i == 1:
            result.append([1, 1])
        else:
            res = result[i - 1]
            length = len(res)
            new = []
            for y in range(length + 1):
                if y == 0 or y == length:
                    new.append(1)
                else:
                    new.append(res[y] + res[y - 1])
            result.append(new)
    return result
