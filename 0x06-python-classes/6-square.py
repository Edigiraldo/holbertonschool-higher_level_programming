#!/usr/bin/python3
"""This module implements the Square class."""


class Square:
    """Class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize size attribute of instance
           the size has to be >= to 0."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (type(position) != tuple or type(position[0]) != int or
           type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """This method returns the area of the square object."""
        return self.__size ** 2

    @property
    def size(self):
        """property that returns the value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter method for set size attribute."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property getter that returns the tuple position."""
        return position

    @position.setter
    def position(self, value):
        """property setter method for set position attribute."""
        if (type(position) != tuple or type(position[0]) != int or
           type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        size = self.__size
        squares = size
        position = self.__position[0]
        while size != 0:
            for i in range(squares):
                if i < position:
                    print(' ', end='')
                else:
                    print('#', end='')
            size -= 1
            print()
        if squares == 0:
            print()