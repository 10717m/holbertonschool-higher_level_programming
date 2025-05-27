#!/usr/bin/python3
"""
Module 7-base_geometry
Contains class BaseGeometry with public instance methods area and integer_validator
"""


class BaseGeometry:
    """
    A class with public instance methods area and integer_validator
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value as a positive integer

        Args:
            name: string representing the name
            value: value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(value, int) or isinstance(value, (tuple, list, set)):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
