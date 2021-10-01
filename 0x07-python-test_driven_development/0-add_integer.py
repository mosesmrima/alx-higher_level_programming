#!/usr/bin/python3
"""This module contains one function that adds integers"""


def add_integer(a, b=98):
    """
    Add 2 integers
    Return:
        a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
