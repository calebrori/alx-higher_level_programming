#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list  to find peak
    Returns: 0 or 1
    """
    size = len(list_of_integers)
    pop_dan = size
    pop = size // 2

    if size == 0:
        return None

    while True:
        pop_dan = pop_dan // 2
        if (pop < size - 1 and
                list_of_integers[pop] < list_of_integers[pop + 1]):
            if pop_dan // 2 == 0:
                pop_dan = 2
            pop = pop + pop_dan // 2
        elif pop_dan > 0 and list_of_integers[pop] < list_of_integers[pop - 1]:
            if pop_dan // 2 == 0:
                pop_dan = 2
            pop = pop - pop_dan // 2
        else:
            return list_of_integers[pop]
