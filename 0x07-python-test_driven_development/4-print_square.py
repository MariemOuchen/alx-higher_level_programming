#!/usr/bin/python3

"""A function that prints a square with the character #."""


def print_square(size):
    """prints a square with the character #.

    args:
        size (int): The size of the square.

    Returns: #.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
