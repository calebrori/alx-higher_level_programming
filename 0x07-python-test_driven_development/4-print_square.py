#!/usr/bin/python3
"""Function that prints a square with the character"""


def print_square(size):
    """Print square with # character

    Args:
        size (int): The height/width of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for c in range(size):
        [print("#", end="") for b in range(size)]
        print("")
