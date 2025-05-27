#!/usr/bin/python3
"""
This module defines the MyList class which inherits from list
and includes a method to print the list sorted in ascending order.
"""

class MyList(list):
    """
    MyList inherits from the built-in list class and adds a method
    to print the list elements in sorted (ascending) order.
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original list."""
        if not all(isinstance(x, int) for x in self):
            raise TypeError("all elements must be integers")
        print(sorted(self))

