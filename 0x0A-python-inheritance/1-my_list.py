#!/usr/bin/python3
"""
this module contains one class: Mylist
"""


class MyList(list):
    """
    class contains one method
    """
    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
