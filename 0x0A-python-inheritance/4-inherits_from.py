#!/usr/bin/python3
"""Inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class

    Args:
        obj (any): checked object
        a_class (type): The class
    Returns:
        True if an object is an inherited instance of a_class
        Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
