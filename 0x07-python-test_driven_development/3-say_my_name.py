#!/usr/bin/env python3

""" This module contains one function that concats names """


def say_my_name(first_name, last_name=""):
    """
    function concat 1st and 2nd name
    Return: none
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
