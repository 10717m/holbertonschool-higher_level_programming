#!/usr/bin/python3
"""Defines a square with private size attribute."""


class Square:
    """Represents a square with size validation."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
