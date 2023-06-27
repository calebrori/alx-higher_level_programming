#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    This prints the first x elements of a list that are integers.

    Parameters:
    my_list (list): The list to be printed
    x (int): The number of elements to access in my_list

    Returns:
    int: The real number of integers printed
    """
    count = 0
    index = 0
    while count < x and index < len(my_list):
        try:
            # Check if the element is an integer
            if isinstance(my_list[index], int):
                # Print the integer
                print("{:d}".format(my_list[index]))
                count += 1
        except:
            # Skip the element if it's not an integer
            pass
        index += 1
    return count
