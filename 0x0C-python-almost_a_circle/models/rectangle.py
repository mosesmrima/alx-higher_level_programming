#!/usr/bin/python3

""" This module contains the rectangle class
    that inherits from the base class """
from models.base import Base


class Rectangle(Base):
    """Rectangle class defination"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method
        params: @width, @height, @x, @y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """public width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """public setter for width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """public height setter"""
        return self.__height

    @height.setter
    def height(self, value):
        """public height getter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """public getter for attr x"""
        return self.__x

    @x.setter
    def x(self, value):
        """public setter for attr x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """public getter for attr y"""
        return self.__y

    @y.setter
    def y(self, value):
        """public setter for attr y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """instance method to calculate the area
        returns: width x height"""
        return self.__width * self.__height

    def display(self):
        """method to print the visual rpresentation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def __str__(self):
        """override the __str__ method"""
        id = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h)

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg == None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif arg == 1:
                    self.width = arg
                elif arg == 2:
                    self.height = arg
                elif arg == 3:
                    self.x = arg
                elif arg == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v == None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return dictionary representation of object"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
