#!/usr/bin/python3

"""A function that checks if an object
    is a sub-class a specified class.
"""


def inherits_from(obj, a_class):
    """chceks if an object is a sub-class
        a specified class.

        Returns: True, if true or False,
                if false.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
