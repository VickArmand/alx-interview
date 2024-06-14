#!/usr/bin/python3
"""0-island_perimeter has function island_perimeter"""


def perimeter_cell(grid, i, j):
    """Determines the perimeter of one cell"""
    rows = len(grid)
    columns = len(grid[i])
    perimeter = 4
    if i == 0 and j == 0:
        if grid[i + 1][j] == 1:
            perimeter -= 1
        if grid[i][j + 1] == 1:
            perimeter -= 1
    elif i == rows - 1 and j != columns - 1:
        if grid[i - 1][j] == 1:
            perimeter -= 1
        if grid[i][j - 1] == 1:
            perimeter -= 1
        if grid[i][j + 1] == 1:
            perimeter -= 1
    elif j == columns - 1 and i != rows - 1:
        if grid[i - 1][j] == 1:
            perimeter -= 1
        if grid[i][j - 1] == 1:
            perimeter -= 1
        if grid[i + 1][j] == 1:
            perimeter -= 1
    elif j == 0 and i != 0:
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
    elif j == columns - 1 and i == rows - 1:
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
    grid_perimeter = 0
    rows = len(grid)
    for i in range(rows):
        columns = len(grid[i])
        for j in range(columns):
            if grid[i][j] == 1:
                cell_perimeter = perimeter_cell(grid, i, j)
                grid_perimeter += cell_perimeter
    return grid_perimeter
