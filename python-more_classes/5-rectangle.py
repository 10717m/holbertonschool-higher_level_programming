#!/usr/bin/python3
"""Defines a Rectangle class with str, repr, and del behavior."""


class Rectangle:
    """Defines a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it's an integer >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it's an integer >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter, or 0 if width or height is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle as a string of '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return string representation recreate new instance with eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when the instance is deleted."""
        print("Bye rectangle...")
