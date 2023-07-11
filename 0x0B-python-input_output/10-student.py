#!/usr/bin/python3
"""Class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student

        Args:
            first_name (str): student first name
            last_name (str): student last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of the student

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {d: getattr(self, d) for d in attrs if hasattr(self, d)}
        return self.__dict__
