#!/usr/bin/python3
"""
module contains one function to check instance of class
"""


def is_kind_of_class(obj, a_class):
    """
    check if object is instance or inherits from a class
    :param obj: object to check
    :param a_class: class to compare to
    :return: true if is instance else false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
