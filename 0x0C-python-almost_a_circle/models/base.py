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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list of objects to a file

        Args:
            list_objs (list): A list of instances inherited from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON string representation

        Args:
            json_string (str): string representing list of dictionaries
        Returns:
            If json_string is None or empty - an empty list
            Otherwise - return list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            **dictionary (dict): double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list
            Otherwise - a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
