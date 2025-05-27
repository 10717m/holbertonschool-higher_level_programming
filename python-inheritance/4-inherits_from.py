#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class that inherits (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherits from a_class,
    but not if obj is exactly an instance of a_class.
    Otherwise, returns False.
    """
    # Check if obj is an instance of a_class or subclass thereof
    if not isinstance(obj, a_class):
        return False
    # Return True only if obj's class is exactly a_class (means it's subclass)
    return type(obj) is not a_class
