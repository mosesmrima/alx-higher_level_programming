#!/usr/bin/python3
"""
This module cntains ol ine class
"""


class Square:
    """
    A class with a private instance variable size
    Also chcks if size an integer and greater than or equal to zero
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        if (not isinstance(pos, tuple) or
                len(pos) != 2 or
                not all(isinstance(num, int) for num in pos) or
                not all(num >= 0 for num in pos)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pos

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
