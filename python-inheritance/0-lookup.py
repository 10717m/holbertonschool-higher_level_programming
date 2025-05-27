#!/usr/bin/python3
"""
lookup for available attributes and methods of an object
"""


def lookup(obj):
    """
    return a list of all available attributes and methods of the given object
    """
    return dir(obj)
