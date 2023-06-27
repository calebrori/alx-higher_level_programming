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
        # Try to convert the value to an integer and print it
        print("{:d}".format(int(value)))

        # Return True if the value is an integer
        return isinstance(value, int)
    except (ValueError, TypeError):
        # Log the error and return False if the value is not an integer
        print("Error: The value is not an integer")
        return False
