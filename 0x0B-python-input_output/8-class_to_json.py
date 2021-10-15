#!/usr/bin/python3

""" This module contains one function """


def class_to_json(obj):
    """convert object to json representation"""
    return obj.__dict__
