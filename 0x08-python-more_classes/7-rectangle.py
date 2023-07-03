#!/usr/bin/python3

"""A class that defines a rectangle."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialises a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets/Sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Gets/Sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """int: The area of the recatngle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """int: The perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Represents a rectangle with a #"""
        tmp = []
        for i in range(self.__height):
            [tmp.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                tmp.append("\n")
        return ("".join(tmp))

    def __repr__(self):
        """Returns the officail representation of the rectangle"""
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        """Deletes an instance and prints a message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
