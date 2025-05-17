#!/usr/bin/python3
"""This module provides a function to print a square with # characters."""


def print_square(size):
    """Print a square with the character #.

    Args:
        size: Size length of the square (must be non-negative integer)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)
