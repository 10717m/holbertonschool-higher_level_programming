#!/usr/bin/python3
"""Module 8-rectangle
Defines Rectangle class with instance counting, customizable print symbol,
and method to compare rectangles by area.
"""


class Rectangle:
    """Rectangle class with width, height, instance counting,
    print symbol, and comparison by area."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """Return the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter or 0 if width or height is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle as a string using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        lines = [symbol * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return string to recreate instance via eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance is deleted and decrement count."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): first rectangle instance.
            rect_2 (Rectangle): second rectangle instance.

        Raises:
            TypeError: if rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: the rectangle with the bigger or equal area (rect_1 if equal).
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an_
