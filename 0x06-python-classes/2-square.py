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
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
