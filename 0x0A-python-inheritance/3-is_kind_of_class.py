#!/usr/bin/python3
"""Class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is exactly an instance of a given class

    Args:
        obj (any): checked object
        a_class (type): The class
    Returns:
        True if the object is exactly an instance of the specified class
        Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
