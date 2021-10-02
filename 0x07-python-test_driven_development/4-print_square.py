#!/usr/bin/env python3

""" This module contains one function to print a square """


def print_square(size):
    """
    print_square: print a square of size ``size``
    param @size: size of the square
    Return: none
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    i = 0
    while i < size:
        j = 0
        while j < size:
            print("#", end="")
            j += 1
        print("")
        i += 1
