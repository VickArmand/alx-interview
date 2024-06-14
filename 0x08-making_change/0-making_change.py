#!/usr/bin/python3
"""
0-making_change module contains
a function called makeChange
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each denomination
    of coin in the list
    """
    if total <= 0:
        return 0
    if sum(coins) > total or len(coins) == 0:
        return -1
    min_coins = 0
    coins.sort()
    while total > 0 and len(coins) != 0:
        max_denomination = coins[-1]
        if total >= max_denomination:
            total -= max_denomination
            min_coins += 1
        else:
            coins.remove(max_denomination)
    return min_coins
