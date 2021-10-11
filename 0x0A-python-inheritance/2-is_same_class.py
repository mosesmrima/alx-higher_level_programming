#!/usr/bin/python3
"""
module contains one function to check instance of class
"""


def is_same_class(obj, a_class):
    """
    function to check if object is instance of a given class
    :param obj:object to check
    :param a_class:clss to check
    :return:True if is instance else, returns false
    """
    if type(obj) == a_class:
        return True
    return False
