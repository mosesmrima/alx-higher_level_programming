#!/usr/bin/python3
""" this module contains one class """


class Student:
    """student class defination"""

    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict repr of self"""
        if type(attrs) is list and all(type(s) is str for s in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
