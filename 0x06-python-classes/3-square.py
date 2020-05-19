#!/usr/bin/python3
"""This module implements the Square class."""


class Square:
    """Class Square."""

    def __init__(self, size=0):
        """Initialize size attribute of instance
           the size has to be >= to 0."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This method returns the area of the square object."""
        return self.__size ** 2
