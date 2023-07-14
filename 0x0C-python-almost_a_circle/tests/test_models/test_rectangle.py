#!/usr/bin/python3

"""Tests for the rectangle module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    def test_rectangle(self):
        self.assertTrue(True)
    
    def test_rectangle_width(self):
        rw = Rectangle(1, 2)
        self.assertEqual(rw.width, 1)

    def test_rectangle_height(self):
        rh = Rectangle(1, 2)
        self.assertEqual(rh.height, 2)

    def test_rectangle_x(self):
        rx = Rectangle(1, 2, 3)
        self.assertEqual(rx.x, 3)

    def test_rectangle_y(self):
        ry = Rectangle(1, 2, 3, 4)
        self.assertEqual(ry.y, 4)

    def test_zero_y(self):
        rz = Rectangle(1, 2, 3, 0,)
        self.assertEqual(rz.y, 0)

    def test_zero_x(self):
        rz = Rectangle(1, 2, 0, 4,)
        self.assertEqual(rz.x, 0)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            rz = Rectangle(0, 2, 3, 4,)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            rz = Rectangle(1, 0, 3, 4,)

    def test_raise_type_error(self):
        with self.assertRaises(TypeError):
            raise TypeError

    def test_raise_value_error(self):
        with self.assertRaises(ValueError):
            raise ValueError

    def test_neg_width_initalised(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_neg_height_assigned(self):
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.height = -2

    def test_neg_height_initalised(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_neg_x_assigned(self):
        r = Rectangle(1, 2, 3)
        with self.assertRaises(ValueError):
            r.x = -3

    def test_neg_x_initalised(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_neg_y_assigned(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r.y = -4

    def test_neg_y_initalised(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_list_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle([], 2, 3)

    def test_list_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, [], 3)

    def test_list_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, [])

    def test_list_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, [])

    def test_tuple_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle({}, 2, 3)

    def test_tuple_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, {}, 3)

    def test_tuple_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, {}, 4)

    def test_tuple_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, {})        

    def test_str_width(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.width = "True"

    def test_str_height(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.height = "True"

    def test_str_x(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.x = "True"
        
    def test_str_y(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.y = "True"

    def test_bool_width(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.width = True

    def test_bool_height(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.height = True

    def test_bool_x(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.x = True
        
    def test_bool_y(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.y = True
    
    def test_none_width(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.width = None

    def test_none_height(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.height = None

    def test_none_x(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.x = None
        
    def test_none_y(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.y = None
    
    def test_infinity_input(self):
        with self.assertRaises(OverflowError):
            r = Rectangle(1, 2, 3, int(float('inf')))

    def test_empty(self):
        with self.assertRaises(TypeError):
            r = Rectangle()
