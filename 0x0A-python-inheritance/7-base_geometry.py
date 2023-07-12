#!/usr/bin/python3
"""A class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): parameter name
            value (int): parameter checked
        Raises:
            TypeError: non-integer value
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
