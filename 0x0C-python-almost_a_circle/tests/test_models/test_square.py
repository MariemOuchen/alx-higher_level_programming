#!/usr/bin/python3
"""Tests for the square module"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests of the square class"""

    def test_square(self):
        self.assertTrue(True)

    def test_sqaure_initialised(self):
        s1 = Square(3)
        self.assertEqual(s1.size, 3)

    def test_sqaure_assign(self):
        s1 = Square(4)
        s1.size = 8
        self.assertEqual(s1.size, 8)

    def test_square_different_values(self):
        s1 = Square(2, 5)
        self.assertEqual(s1.size, 2)

    def test_square_string(self):
        with self.assertRaises(TypeError):
            s1 = Square("2")

    def test_square_empty(self):
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_square_dict(self):
        with self.assertRaises(TypeError):
            s1 = Square({3, 2})

    def test_square_list(self):
        with self.assertRaises(TypeError):
            s1 = Square([3, 2])

    def test_square_tuple(self):
        with self.assertRaises(TypeError):
            s1 = Square((3, 2))

    def test_square_zero(self):
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_square_second_zero(self):
        s1 = Square(2, 0)
        self.assertEqual(s1.size, 2)

    def test_square_second_zero(self):
        s1 = Square(2, 5)
        self.assertEqual(s1.size, 2)
