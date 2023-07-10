#!/usr/bin/python3

"""a class MyList that inherits from list class"""


class MyList(list):
    """A subclass of list"""

    def print_sorted(self):
        """Sorts and prints the list"""

        tmp = sorted(self)
        print(tmp)
