#!/usr/bin/python3

"""This module has TestRectangle class to test the Rectangle class"""

import unittest

from models.rectangle import (Rectangle, Base)


class TestRectangle(unittest.TestCase):
    """This class is for testing Rectangle class attributes and functions"""

    def setUp(self) -> None:
        """Setup data before each test method"""

        Base._Base__nb_objects = 0

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

    def test_area(self):
        """Tests the area of the rectangle"""

        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

        r.width = 2
        r.height = 10
        self.assertEqual(r.area(), 20)

        r.width = 7
        r.height = 8
        self.assertEqual(r.area(), 56)

    def test_str(self):
        """Tests the __str__ method"""

        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        r = Rectangle(5, 5, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 1/0 - 5/5")

        r = Rectangle(height=3, width=7, id=15, y=3, x=4)
        self.assertEqual(r.__str__(), "[Rectangle] (15) 4/3 - 7/3")
