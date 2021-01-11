#!/usr/bin/python3
"""
This module contains one Rectangle class
"""


class Rectangle:
    """
    A class rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle
        Args:
        :param width: rectangle's width
        :param height: rectangle's height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        height getter/setter
        :return:
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter/ setter
        :return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        :return: returns area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        method to calculate the perimeter of a rectangle
        :return: perimeter or ) if width || height is zero
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        :return: a rectangle represented by #
        """
        if self.__width == 0 or self.__height:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)
