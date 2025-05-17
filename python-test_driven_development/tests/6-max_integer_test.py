#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for testing max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list with max value at the beginning"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list"""
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_single_element_list(self):
        """Test a list with a single element"""
        single = [7]
        self.assertEqual(max_integer(single), 7)

    def test_floats(self):
        """Test a list of floats"""
        floats = [1.5, 2.7, 0.8, 3.14]
        self.assertEqual(max_integer(floats), 3.14)

    def test_mixed_types(self):
        """Test a list with mixed int and float types"""
        mixed = [1, 2.5, 3, 4.2]
        self.assertEqual(max_integer(mixed), 4.2)

    def test_negative_numbers(self):
        """Test a list of negative numbers"""
        negatives = [-1, -5, -3, -2]
        self.assertEqual(max_integer(negatives), -1)

    def test_duplicate_values(self):
        """Test a list with duplicate values"""
        duplicates = [3, 3, 3, 3]
        self.assertEqual(max_integer(duplicates), 3)

    def test_string(self):
        """Test a string (which is iterable)"""
        string = "hello"
        self.assertEqual(max_integer(string), 'o')

    def test_list_of_strings(self):
        """Test a list of strings"""
        strings = ["hello", "world", "python"]
        self.assertEqual(max_integer
