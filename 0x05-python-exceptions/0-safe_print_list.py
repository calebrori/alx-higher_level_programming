#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    This function prints x elements of a list and returns the real number of elements printed.

    Parameters:
    my_list (list): The list to be printed
    x (int): The number of elements to print

    Returns:
    int: The real number of elements printed
    """
    try:
        pop = 0
        for c in range(x):
            print(my_list[c], end="")
            pop += 1
        print()
        return pop
    except IndexError:
        print()
        return pop
