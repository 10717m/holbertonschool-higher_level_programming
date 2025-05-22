#!/usr/bin/python3
"""declare a private class attribute (variable) to return size"""


class Square:
    """a class to represent Square"""
    __size = 0

    def __init__(self, size=0):
        """an instance variable to accept the size with validating input"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
