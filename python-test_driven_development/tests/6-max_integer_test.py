#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Checks the code - tests"""

    def test_basic(self):
        """Basic use"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_max_at_end(self):
        """Max at the end"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_at_beginning(self):
        """Max at the beginning"""
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_in_middle(self):
        """Max in the middle"""
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_negative_number(self):
        """Negative number in the list"""
        self.assertEqual(max_integer([-1, 2, 1]), 2)

    def test_only_negative_numbers(self):
        """Only negative numbers in the list"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_one_element(self):
        """List of one element"""
        self.assertEqual(max_integer([3]), 3)

    def test_empty_list(self):
        """List is empty"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
