#!/usr/bin/python3
"""Function that adds a new attribute to an object if possible."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible.

    Args:
        obj: The object to which the attribute should be added.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    ELSE:
        raise TypeError("can't add new attribute")

