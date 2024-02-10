#!/usr/bin/python3

"""This module has TestRectangle class to test the Rectangle class"""

import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class is for testing Rectangle class attributes and functions"""

    def test_width(self):
        """Tests the width of the rectangle"""

        r = Rectangle(10, 15)
        self.assertEqual(r.width, 10)

        r.width = 3
        self.assertEqual(r.width, 3)

        with self.assertRaises(TypeError):
            r.width = "5"

        with self.assertRaises(TypeError):
            r.width = None

        with self.assertRaises(TypeError):
            r.width = 1.1

        with self.assertRaises(ValueError):
            r.width = -5

        with self.assertRaises(ValueError):
            r.width = 0

    def test_height(self):
        """Tests the height of the rectangle"""

        r = Rectangle(10, 15)
        self.assertEqual(r.height, 15)

        r.height = 3
        self.assertEqual(r.height, 3)

        with self.assertRaises(TypeError):
            r.height = "5"

        with self.assertRaises(TypeError):
            r.height = None

        with self.assertRaises(TypeError):
            r.height = 1.1

        with self.assertRaises(ValueError):
            r.height = -5

        with self.assertRaises(ValueError):
            r.height = 0

    def test_x(self):
        """Tests x of the rectangle"""

        r = Rectangle(10, 15, x=5)
        self.assertEqual(r.x, 5)

        r.x = 0
        self.assertEqual(r.x, 0)

        with self.assertRaises(TypeError):
            r.x = "5"

        with self.assertRaises(TypeError):
            r.x = None

        with self.assertRaises(TypeError):
            r.x = 1.1

        with self.assertRaises(ValueError):
            r.x = -5

    def test_y(self):
        """Tests y of the rectangle"""

        r = Rectangle(10, 15, y=7)
        self.assertEqual(r.y, 7)

        r.y = 0
        self.assertEqual(r.y, 0)

        with self.assertRaises(TypeError):
            r.y = "5"

        with self.assertRaises(TypeError):
            r.y = None

        with self.assertRaises(TypeError):
            r.y = 1.1

        with self.assertRaises(ValueError):
            r.y = -5
