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
        """convert class attriutes to dictionary"""
        if (type(attrs) is list) and (all(type(el) is str for el in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """use a dictionary string to instantiate an object"""
        for key, val in json.items():
            setattr(self, key, val)
