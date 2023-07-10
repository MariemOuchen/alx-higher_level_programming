#!/usr/bin/python3

"""A function that check if object is exactly
    an instance of the specified class

    Returns:
        True, if both obects are the same, else
         it returns False
"""


def is_same_class(obj, a_class):
    """Checks if bject is exactly an instance
        of the specified class

        Return: True, if true or False, if false
    """

    if type(obj) == a_class:
        return True
    else:
        return False
