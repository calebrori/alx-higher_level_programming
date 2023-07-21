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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts

        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
