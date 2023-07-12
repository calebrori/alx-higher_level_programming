#!/usr/bin/python3
"""Class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """New square initialized

        Args:
            size (int): New square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
