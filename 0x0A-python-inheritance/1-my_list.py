#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Implements sorted printing"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
