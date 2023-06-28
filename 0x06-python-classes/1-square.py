#!/usr/bin/python3

class Square:
    """
    This class defines a square by its size.
    """
    def __init__(self, size):
        """
        Initializes new instance of class

        Parameters:
        size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the size of the square

        Returns:
        int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Parameters:
        value (int): The new size of the square
        """
        self.__size = value
