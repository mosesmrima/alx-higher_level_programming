#!/usr/bin/python3
"""
This module cntains ol ine class
"""


class Square:
    """
    A class with a private instance variable size
    Also chcks if size an integer and greater than or equal to zero
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size
