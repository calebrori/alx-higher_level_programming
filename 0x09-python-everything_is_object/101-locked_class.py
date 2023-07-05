#!/usr/bin/python3
"""This is a LockedClass with no class or object attribute"""


class LockedClass:
    """
     This prevents the user from dynamically
     creating new instance attributes.
    """

    __slots__ = ["first_name"]
