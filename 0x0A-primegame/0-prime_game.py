#!/usr/bin/python3
"""
module 0-prime_game has a function isWinner

Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.
They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""


def isPrime(num):
    """confirms if a number is prime or not"""
    if num == 0 or num == 1:
        return False
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    return prime


def remove_multiples(numList, num):
    """
    Removes multiples of a num in a list
    """
    for elem in numList:
        if elem > 1 and elem % num == 0:
            numList.remove(elem)


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    Example:

    x = 3, nums = [4, 5, 1]
    First round: 4

    Maria picks 2 and removes 2, 4, leaving 1, 3
    Ben picks 3 and removes 3, leaving 1
    Ben wins because there are no prime numbers left for Maria to choose
    Second round: 5

    Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    Ben picks 3 and removes 3, leaving 1, 5
    Maria picks 5 and removes 5, leaving 1
    Maria wins because there are no prime numbers left for Ben to choose
    Third round: 1

    Ben wins because there are no prime numbers for Maria to choose
    """
    players = ['Maria', 'Ben']
    wins = {'Maria': 0, 'Ben': 0}
    for round in range(x):
        element = nums[round]
        numList = [*range(1, element + 1)]
        for j in range(2):
            for num in numList:
                iP = isPrime(num)
                if iP:
                    # print(round, num, element, players[j], 'old_l', numList)
                    remove_multiples(numList, num)
                    wins[players[j]] = 1
                    wins[players[1-j]] = 0
            # print(round, num, element, players[j], 'new_l', numList)
    # print(wins)
    max = 0
    winner = None
    for player in players:
        if wins[player] > max:
            max = wins[player]
            winner = player
    return winner
