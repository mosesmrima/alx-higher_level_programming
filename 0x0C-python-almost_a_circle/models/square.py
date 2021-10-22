#!/usr/bin/python3

""" This module contains the Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class defination,
    Inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """init method of Squre class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """public getter for size attr"""
        return self.width

    @size.setter
    def size(self, value):
        """public setter for size attr"""
        self.width = value
        self.height = value

    def __str__(self):
        """overloads the str method"""
        w = self.width
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, w)

    def update(self, *args, **kwargs):
        """update attributes with new values"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return dictionary representation of instance"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
