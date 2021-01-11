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
