#!/usr/bin/python3
"""
This module has a function that solves N queens problem
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard
"""
import sys
queen_positions = []
previous_positions = []


def check_attackable(x, y, occupied_positions):
    """
    This function finds out if the queen is attackable
    i.e: not in same row, column or diagonal
    if attackable return True
    otherwise False
    """
    for position in occupied_positions:
        x_position = position[0]
        y_position = position[1]
        if x_position == x or y_position == y:
            return True
        x_diff = abs(x_position - x)
        y_diff = abs(y_position - y)
        if x_diff == y_diff:
            return True
    return False


def is_valid_list(positions):
    """
    Confirms whether each queen is assigned a position in
    accordance with the right standards
    """
    for position in positions:
        is_valid= check_attackable(position[0], position[1], positions)
        if not is_valid:
            return False
    return True

def backtrack(previous_positions, n):
    new_positions = []
    for position in previous_positions:
        previous_positions_copy = previous_positions.copy()
        previous_positions_copy.remove(position)
        i = position[0]
        for j in range(n):
            attackable = check_attackable(i, j, previous_positions_copy)
            if not attackable and [i, j] not in previous_positions:
                new_positions.append([i, j])
        print(new_positions)
        print(previous_positions_copy)
        # new_positions.clear()
    is_valid = is_valid_list(new_positions)
    # print("original", is_valid, new_positions)
    if len(new_positions) == n and is_valid:
        return new_positions
    else:
        backtrack(new_positions, n)

def nqueens(n):
    """
    N must be an integer greater or equal to 4
    """
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    global previous_positions
    global queen_positions
    if len(previous_positions) > 0:
        queen_positions = backtrack(previous_positions, n)
    else:
        for i in range(n):
            for j in range(n):
                attackable = check_attackable(i, j, queen_positions)
                if not attackable:
                    queen_positions.append([i, j])
        if len(queen_positions) != n:
            previous_positions = queen_positions.copy()
            queen_positions.clear()
            nqueens(n)
    return queen_positions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = sys.argv[1]
    try:
        n = int(n)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    for times in range(n):
        q = nqueens(n)
        print('[', end="")
        for i in range(len(q)):
            if i > 0 and (i + 1) % n == 0:
                print(f'{q[i]}]')
            else:
                print(q[i], end="")
