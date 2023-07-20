#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor initializes new Square

        Args:
            size (int): Square size
            x (int): Square x axis
            y (int): Square y axis
            id (int): Square identity
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Puts the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
