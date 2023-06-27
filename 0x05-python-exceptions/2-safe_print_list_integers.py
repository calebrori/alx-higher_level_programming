#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    This prints the first x elements of a list that are integers.

    Parameters:
    my_list (list): The list to be printed
    
    Returns:
    The real number of integers printed
    """
    pop = 0
    for c in range(0, x):
        try:
            print("{:d}".format(my_list[c]), end="")
            pop += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (pop)
