#!/usr/bin/python3
"""Module for class Rectangle inherited from Base class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances with width, height, x, y, id attr."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width private variable."""
        return self.__width

    @property
    def height(self):
        """Getter method for height private variable."""
        return self.__height

    @property
    def x(self):
        """Getter method for x private variable."""
        return self.__x

    @property
    def y(self):
        """Getter method for y private variable."""
        return self.__y

    @width.setter
    def width(self, width):
        """Setter method for width private variable."""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Setter method for height private variable."""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Setter method for x private variable."""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Setter method for y private variable."""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for k in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end='')
            for i in range(self.width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """update fields of object."""
        len_args = len(args)
        if len_args > 0:
            self.id = args[0]
        if len_args > 1:
            self.width = args[1]
        if len_args > 2:
            self.height = args[2]
        if len_args > 3:
            self.x = args[3]
        if len_args > 4:
            self.y = args[4]

        keys = kwargs.keys()
        if "width" in keys:
            self.width = kwargs["width"]
        if "height" in keys:
            self.height = kwargs["height"]
        if "x" in keys:
            self.x = kwargs["x"]
        if "y" in keys:
            self.y = kwargs["y"]
        if "id" in keys:
            self.id = kwargs["id"]

    def __str__(self):
        "Function for print"
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
               self.id, self.x, self.y, self.width, self.height))

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        dic = {"id": self.id, "width": self.width, "height": self.height,
               "x": self.x, "y": self.y}
        return dic
