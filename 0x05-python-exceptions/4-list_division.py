#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.

    Args:
        my_list_1 (list): The first list to divide.
        my_list_2 (list): The second list to divide.
        list_length (int): The length of the resulting list.

    Returns:
        list: A new list (length = list_length) with all divisions.

    Raises:
        TypeError: If an element is not an integer or float.
        ZeroDivisionError: If the denominator is zero.
        IndexError: If my_list_1 or my_list_2 is too short.

    Prints:
        An error message if an error occurs.

    """
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if type(a) not in [int, float] or type(b) not in [int, float]:
                raise TypeError("wrong type")
            if b == 0:
                raise ZeroDivisionError("division by 0")
            result.append(a / b)
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        finally:
            pass
    return result
