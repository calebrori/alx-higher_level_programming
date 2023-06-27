#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division, or None

    Raises:
        ZeroDivisionError: If the denominator is zero.
        TypeError: If either input is not an integer.

    Prints:
        The result of the division, or an error message
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Both inputs must be integers")
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
