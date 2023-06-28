#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """This class defines a square by its size"""

    def __init__(self, size):
        """Initialize a new Square.

        Params:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
