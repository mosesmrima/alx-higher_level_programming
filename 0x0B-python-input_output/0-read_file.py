#!/usr/bin/python3

""" this module contains one function """


def read_file(filename=""):
    """function to read a file"""
    with open(filename, encoding="utf-8") as my_file:
        data = my_file.read()
        print(data.strip())
