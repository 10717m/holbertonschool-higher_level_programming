#!/usr/bin/python3
"""
Module that defines a Student class
with a method to retrieve dictionary representation.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the instance.

        Args:
            attrs (list): List of attribute names to include.
        Returns:
            dict: Dictionary of attributes.
        """
        if isinstance(attrs, list) and all(isinstance(k, str) for k in attrs):
            return {
                k: getattr(self, k)
                for k in attrs
                if hasattr(self, k)
            }
        return self.__dict__
