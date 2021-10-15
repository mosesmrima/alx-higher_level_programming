#!/usr/bin/python3
""" this module contains one class """


class Student:
    """studet class defination"""

    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return json repr of object"""
        return self.__dict__
