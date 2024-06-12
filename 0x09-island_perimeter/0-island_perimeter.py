#!/usr/bin/python3
"""0-island_perimeter has function island_perimeter"""


def perimeter_cell(grid, i, j):
    """Determines the perimeter of one cell"""
    size = len(grid)
    perimeter = 4
    if j == 0 and i != 0:
        if grid[i + 1][j] == 1:
            perimeter -= 1
        if grid[i][j + 1] == 1:
            perimeter -= 1
        if grid[i - 1][j] == 1:
            perimeter -= 1
    elif i == 0 and j != 0:
        if grid[i + 1][j] == 1:
            perimeter -= 1
        if grid[i][j + 1] == 1:
            perimeter -= 1
        if grid[i][j - 1] == 1:
            perimeter -= 1
    elif i == 0 and j == 0:
        if grid[i + 1][j] == 1:
            perimeter -= 1
        if grid[i][j + 1] == 1:
            perimeter -= 1
    elif i == 0 and j == 0:
        if grid[i + 1][j] == 1:
            perimeter -= 1
        if grid[i][j + 1] == 1:
            perimeter -= 1
    elif i == size - 1 and j != size - 1:
        if grid[i - 1][j] == 1:
            perimeter -= 1
        if grid[i][j - 1] == 1:
            perimeter -= 1
        if grid[i][j + 1] == 1:
            perimeter -= 1
    elif j == size - 1 and i != size - 1:
        if grid[i - 1][j] == 1:
            perimeter -= 1
        if grid[i][j - 1] == 1:
            perimeter -= 1
        if grid[i + 1][j] == 1:
            perimeter -= 1
    elif j == size - 1 and i == size - 1:
        if grid[i - 1][j] == 1:
            perimeter -= 1
        if grid[i][j - 1] == 1:
            perimeter -= 1
    else:
        if grid[i + 1][j] == 1:
            perimeter -= 1
        if grid[i - 1][j] == 1:
            perimeter -= 1
        if grid[i][j + 1] == 1:
            perimeter -= 1
        if grid[i][j - 1] == 1:
            perimeter -= 1
    return perimeter


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes”
    (water inside that isn’t connected to the water surrounding the island).
    """
    perimeter = 0
    size = len(grid)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                val = perimeter_cell(grid, i, j)
                print(val, i, j)
                perimeter += val
    return perimeter
