#!/usr/bin/python3

"""Defines a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises a new rectangle

        args:
            width (int): The width of the rectangle:
            height (int): The height of the rectangle.
            x (int): x
            y (int): y
        """
        super().__init__(id)

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.x, self.y, self.__width, self.__height)

    @classmethod
    def integer_validator(self, name, value):
        """Validate all integer inputs

        args:
            name (str): The name of the object.
            value (int): The value to be validated.

        raises:
            TypeError: If type is not int.
            ValueError: If value is < 0 for x and y,
                        or if value is <= 0 for width
                        and height.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """width (int): The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """height (int): The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """x (int): The x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y (int): The y value of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """(int): Returns the area of a rectangle"""

        return (self.__width * self.__height)

    def display(self):
        """Prints '#' to the stdout"""

        if self.__y > 0:
            for i in range(self.__y):
                print()

        for i in range(self.__height):
            [print(' ', end="") for i in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print("")

    def update(self, *args, **kwargs):
        """Updates the attributes with variable arguments"""

        if args:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                if a == 1:
                    self.__width = arg
                if a == 2:
                    self.__height = arg
                if a == 3:
                    self.__x = arg
                if a == 4:
                    self.__y = arg
                a += 1

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""
        tmp_dict = {
                "id": self.id,
                "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
        return tmp_dict
