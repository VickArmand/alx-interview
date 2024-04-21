#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def getKeys(boxes, index, unlocked, locked):
    """gets the keys in a box in a hierachical manner"""
    unlockedBoxes = set()
    lockedBoxes = set()
    unlockedBoxes.update(unlocked)
    lockedBoxes.update(locked)
    lockedBoxes.remove(index)
    unlockedBoxes.add(index)
    for key in boxes[index]:
        lockedBoxes.add(key)
    for box in lockedBoxes:
        if box not in unlockedBoxes:
            return getKeys(boxes, box, unlockedBoxes, lockedBoxes)
    return unlockedBoxes


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened.
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    unlockedSet = set()
    unlockedSet.add(0)
    keys = getKeys(boxes, 0, unlockedSet, unlockedSet)
    if len(keys) == len(boxes):
        return True
    return False
