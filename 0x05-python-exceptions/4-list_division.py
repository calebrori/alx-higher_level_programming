#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    This function divides element by element 2 lists.

    Parameters:
    my_list_1 (list): The first list
    my_list_2 (list): The second list
    list_length (int): The length of the new list

    Returns:
    list: A new list with element-wise division of the two input lists

    Raises:
    TypeError: If an element in either list is not an integer or float
    ZeroDivisionError: If division by zero occurs
    IndexError: If either list is too short

    """
    new_list = []
    for i in range(list_length):
        try:
            # Check if both lists have elements at the current index
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("Out of range")

            # Check if both elements are numbers
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                raise TypeError("Wrong type")

            # Check if the divisor is zero
            if my_list_2[i] == 0:
                raise ZeroDivisionError("Division by zero")

            # Calculate and append the quotient
            new_list.append(my_list_1[i] / my_list_2[i])
        except IndexError as e:
            # Log the error
            print(f"Error: {e}")
            print("Out of range")
            new_list.append(0)
        except TypeError as e:
            # Log the error
            print(f"Error: {e}")
            print("Wrong type")
            new_list.append(0)
        except ZeroDivisionError as e:
            # Log the error
            print(f"Error: {e}")
            print("Division by zero")
            new_list.append(0)
        finally:
            # Continue to the next iteration
            continue

    return new_list
