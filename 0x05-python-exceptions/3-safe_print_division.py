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
        # Divide the two numbers
        result = a / b
    except ZeroDivisionError as e:
        # Log the error
        print(f"Error: {e}")
        return None
    else:
        # Return the result of the division
        return result
    finally:
        # Print the result of the division
        print("Inside result: {}".format(result))
