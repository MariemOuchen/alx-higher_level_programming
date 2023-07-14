#!/usr/bin/python3

"""Unittests for base class
"""

import unittest
from models.base import Base



class TestBaseClass(unittest.TestCase):
    """Test the base class"""

    def test_id_assign(self):
        """Tests the assignment of id is accurate"""
        tmp = Base(5)
        self.assertEqual(tmp.id, 5)

    def test_id_increment(self):
        """Tests that id increments on instance intiation"""
        tmp = Base()
        tmp2 = Base()
        self.assertEqual(tmp2.id, 2)
