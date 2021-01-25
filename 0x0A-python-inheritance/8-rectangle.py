#!/usr/bin/python3
"""
module contains one empty class
"""


class BaseGeometry:
    """
    class with one method
    """
    def area(self):
        """
        method raises exception
        :return: does not return
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate int method
        :param name: name of side
        :param value: size
        :return: does not return
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    rectangle class
    """
    def __init__(self, width, height):
        """
        init method
        :param width: width of rectangle
        :param height: height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
