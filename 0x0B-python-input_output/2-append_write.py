#!/usr/bin/python3

""" this module contains 1 function """


def append_write(filename="", text=""):
    """function to append to a file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
