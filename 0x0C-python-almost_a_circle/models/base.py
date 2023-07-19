#!/usr/bin/python3

"""Foundation base model class for other classes"""
import json
import csv
import turtle


class Base:
    """Represents Base model

    Private Class Attributes:
        __nb_object (int): keeps track of the number of
        instantiated number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new Base

        Args:
            id (int):  new Base identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
