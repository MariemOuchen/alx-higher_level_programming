#!/usr/bin/python3

""" Defines a Rectangle class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """initialised a new square"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """(int): The area of the square"""

        return (self.__size * self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
