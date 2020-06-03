#!/usr/bin/python3
""""Module for Rectangle class."""


class BaseGeometry:
    """BaseGeometry class."""
    def area(self):
        """raise a exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value. It has to be an
        integer greater than zero."""
        if type(value) != int:
            raise Exception("{} must be an integer".format(name))
        elif value <= 0:
            raise Exception("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Init method for Rectangle class.
        initialize width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns description."""
        return "[Rectangle] ""{}/{}".format(self.__width, self.__height)
