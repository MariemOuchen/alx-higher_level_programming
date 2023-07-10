#!/usr/bin/python3

"""A function that checks if a object is an instnce
    of a class or inherites from it
"""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance of a class
        or inherites from it.

        Returns: True, if true or False, if false.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
