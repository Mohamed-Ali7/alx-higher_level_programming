#!/usr/bin/python3

"""This module has TestRectangle class to test the Rectangle class"""

import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class is for testing Rectangle class attributes and functions"""

    def test_width(self):
        """Tests the width of the rectangle"""

        r = Rectangle(10, 15)
        self.assertEqual(r.wdith, 10)

    def test_height(self):
        """Tests the height of the rectangle"""

        r = Rectangle(10, 15)
        self.assertEqual(r.height, 15)

    def test_x(self):
        """Tests x of the rectangle"""

        r = Rectangle(10, 15, x=5)
        self.assertEqual(r.x, 5)

    def test_y(self):
        """Tests y of the rectangle"""

        r = Rectangle(10, 15, y=7)
        self.assertEqual(r.y, 7)
