#!/usr/bin/python3

def raise_exception():
    """
    This function raises a TypeError exception.

    Raises:
    TypeError: Always raised when the function is called.
    """
    try:
        # Raise a TypeError exception
        raise TypeError("This is a TypeError exception")
    except TypeError as e:
        # Log the error
        print(f"Error: {e}")
