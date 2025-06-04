#!/usr/bin/python3
"""
This module provides a function that returns the dictionary
representation of a simple data structure for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization.
    """
    return obj.__dict__
