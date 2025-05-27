#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """BaseGeometry class with an area method that raises an Exception."""

    def area(self):
        """Raises an Exception indicating that the area method implemented."""
        raise Exception("area() is not implemented")
