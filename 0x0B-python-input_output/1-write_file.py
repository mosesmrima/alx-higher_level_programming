#!/usr/bin/python3

""" this module contains one function """


def write_file(filename="", text=""):
    """function to write to a file"""

    with open(filename, encoding="utf-8", mode="w") as f:
        return f.write(text)
