#!/usr/bin/python3
"""Module for add_attribute function."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible.

    Args:
        obj: The object to which the attribute will be added.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

