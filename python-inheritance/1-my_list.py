#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """Print the list in ascending sorted order (without modifying original list)."""
        print(sorted(self))

