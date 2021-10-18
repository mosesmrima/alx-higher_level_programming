#!/usr/bin/pyton3

""" this modulecontains one function to insert line to a file """


def append_after(filename="", search_string="", new_string=""):
    """insert line to a file after line that matches string"""
    with open(filename, encoding="utf-8", mode="r") as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            i += 1
            if search_string in line:
                lines.insert(i, new_string)
    with open(filename, encoding="utf-8", mode="w") as f:
        f.writelines(lines)
