#!/usr/bin/python3

""" This module contains one function """
import json


def load_from_json_file(filename):
    """create object from json file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
