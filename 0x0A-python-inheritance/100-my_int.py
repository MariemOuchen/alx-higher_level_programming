#!/usr/bin/python3

"""Defines a Class MyInt that inherits from int."""


class MyInt(int):
    """Represents a Class MyInt that inherits from int"""

    def __init__(self, value):
        """Initialises an instance of MyInt"""

        self.value = value

    def __eq__(self, other):
        """Overides and inverts the == operator"""

        return int(self) != other

    def __ne__(self, other):
        """Overides and inverts the != operator"""

        return int(self) == other
