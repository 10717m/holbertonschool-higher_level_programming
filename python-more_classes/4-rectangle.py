#!/usr/bin/python3
"""Module 4-rectangle
Defines a Rectangle class with width, height, area, perimeter,
string representation, and ability to recreate instances via eval().
"""


class Rectangle:
    """Rectangle class defines a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle as a string using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        rows = ['#' * self.width for _ in range(self.height)]
        return "\n".join(rows)

    def __repr__(self):
        """Return a string representation to recreate a new instance."""
        return f"Rectangle({self.width}, {self.height})"

