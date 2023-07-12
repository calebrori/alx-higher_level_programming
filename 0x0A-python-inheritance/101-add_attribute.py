#!/usr/bin/python3
"""Function that adds a new attribute to an object"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible

    Args:
        obj (any): Object to be added attribute
        att (str): name of the attribute
        value (any): The value of attribute
    Raises:
        TypeError: If the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
