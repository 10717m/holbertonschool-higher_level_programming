#!/usr/bin/python3
"""
This module defines the MyList class which inherits from list
and includes a method to print the list sorted in ascending order.
"""

class MyList(list):
    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original list."""
        print(sorted(self))

