#!/usr/bin/python3

""" this module contains one function """

import json


def from_json_string(my_str):
    """convert json obect to string"""

    return json.loads(my_str)
