#!/usr/bin/python3
"""Module 102-square
Defines a Square class that supports comparisons by area.
"""


class Square:
    """Represents a square that supports size validation and comparisons."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.

        Args:
            size (int or float): The size of one side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if square areas are equal."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Check if square areas are not equal."""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """Check if this square is less than another based on area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Check if this square less than or equal another based on area."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """Check if this square is greater than another based on area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Check if this square is greater than or equal another based area."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
