#!/usr/bin/python3
"""This defines a rectangle"""


class Rectangle:
    """A rectangle representation"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Define width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width should be an integer")
        if value < 0:
            raise ValueError("width should be >= 0")
        self.__width = value

    @property
    def height(self):
        """Define height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height should be an integer")
        if value < 0:
            raise ValueError("height should be >= 0")
        self.__height = value