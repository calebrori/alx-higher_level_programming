#!/usr/bin/python3
"""Function that returns the dictionary
description with simple data structure"""


def class_to_json(obj):
    """Return dictionary represntation of a data structure"""
    return obj.__dict__
