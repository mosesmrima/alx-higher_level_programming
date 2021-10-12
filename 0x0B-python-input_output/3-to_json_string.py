#!/usr/bin/python3

""" this module contains 1 function """
import json


def to_json_string(my_obj):
    """dump object to json string"""
    return json.dumps(my_obj)
