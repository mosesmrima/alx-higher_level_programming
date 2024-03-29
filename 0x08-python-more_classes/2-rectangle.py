#!/usr/bin/python3

"""This module contains the Rectangle class """


class Rectangle:
    """ rectangle class """
    def __init__(self, width=0, height=0):
        """init method for optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the triangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
