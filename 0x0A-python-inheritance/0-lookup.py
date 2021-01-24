#!/usr/bin/python3
"""
this module contains one method
"""


def lookup(obj):
    """
    :param obj: the object to look up its available params and methods
    :return :a list of all available methods and attributes of an object
    """
    return dir(obj)
