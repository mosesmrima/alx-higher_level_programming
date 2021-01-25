#!/usr/bin/python3
"""
module contains one function to check instance of class
"""


def inherits_from(obj, a_class):
    """
    function to see if an object inherits from a subclass
    :param obj: the object to check
    :param a_class: the class to check subclass from
    :return: True if object inherits from subclass else, false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
