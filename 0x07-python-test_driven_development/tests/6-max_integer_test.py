#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests the 'max_integer' function"""

    def test_empty_list(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_ordered(self):
        ordered = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)

    def test_unordered(self):
        unordered_list = [5, 3, 1, 8]
        self.assertEqual(max_integer(unordered_list), 8)

    def test_float(self):
        list_with_floats = [5.6, 3, 1, 8.6]
        self.assertEqual(max_integer(list_with_floats), 8.6)

    def test_float_only(self):
        f_only = [4.5, 36.6, 6.3]
        self.assertEqual(max_integer(f_only), 36.6)

    def test_negative_values(self):
        neg_list = [-1, -5, -8, -4]
        self.assertEqual(max_integer(neg_list), -1)

    def test_type(self):
        self.assertIsInstance(max_integer(list=[4, 8, 6]), int)

    def test_string(self):
        string = "a string"
        self.assertEqual(max_integer(string), "t")

    def test_single_element(self):
        element = [9]
        self.assertEqual(max_integer(element), 9)

if __name__ == '__main__':
    unittest.main()
