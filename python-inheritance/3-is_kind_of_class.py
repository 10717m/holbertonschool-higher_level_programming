#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a given class or a subclass thereof.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass of a_class.
    Otherwise, returns False.
    """
    return isinstance(obj, a_class)

