#!/usr/bin/python3

"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Represents a class BaseGeometry"""

    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value

        args:
            name (string): The name of the item to be valitdated.
            value (int): The value ti be validated.

        raises:
            ypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
