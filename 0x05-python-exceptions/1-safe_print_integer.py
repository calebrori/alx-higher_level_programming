#!/usr/bin/python3

def safe_print_integer(value):
    """
    This takes a value as argument and prints it as an integer

    Parameters:
    value (any): The value to be printed as an integer

    Returns:
    bool: True if the value is an integer, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
