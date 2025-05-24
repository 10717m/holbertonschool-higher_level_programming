#!/usr/bin/python3
"""Module 6-square
Defines a Square class with size, position, area calculation, visual printing.
"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position to offset the square when printed.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int): Size of the square. Defaults to 0.
            position (tuple): Tuple of 2 positive integers. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character considering position.

        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset (newlines)
        print("\n" * self.__position[1], end="")

        # Print the square lines with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
