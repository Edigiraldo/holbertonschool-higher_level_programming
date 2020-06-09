#!/usr/bin/python3
"""Module for square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square object with size, x, y."""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """"returns the size field."""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter method for size private variable."""
        self.width = size
        self.height = size
        self.__size = size

    def __str__(self):
        """function to print."""
        return ("[Square] ({}) {}/{} - {}".format(
               self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """update fields of object."""
        len_args = len(args)
        if len_args > 0:
            self.id = args[0]
        if len_args > 1:
            self.size = args[1]
        if len_args > 2:
            self.x = args[2]
        if len_args > 3:
            self.y = args[3]

        if len_args > 0:
            kwargs = {}
        keys = kwargs.keys()
        if "size" in keys:
            self.size = kwargs["size"]
        if "x" in keys:
            self.x = kwargs["x"]
        if "y" in keys:
            self.y = kwargs["y"]
        if "id" in keys:
            self.id = kwargs["id"]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        dic = {"id": self.id, "size": self.size,
               "x": self.x, "y": self.y}
        return dic
