#!/usr/bin/python3
"""Module with Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        # Initialize the Rectangle with width and height equal to size
        super().__init__(size, size)

    # area() is inherited from Rectangle and works correctly

    # __str__ is inherited from Rectangle and will print [Rectangle] size/size
