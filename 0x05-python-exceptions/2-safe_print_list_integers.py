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
    for i in my_list:
        try:
            print("{:d}".format(i), end=' ')
            count += 1
        except (ValueError, TypeError):
            pass
        if count == x:
            break
    print()
    return count
