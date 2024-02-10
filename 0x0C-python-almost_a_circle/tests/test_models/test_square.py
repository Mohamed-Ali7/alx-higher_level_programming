#!/usr/bin/python3

"""This module has TestSquare class to test the Square class"""

import unittest

from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """This class is for testing Square class attributes and functions"""

    def setUp(self) -> None:
        """Setup data before each test method"""

        Base._Base__nb_objects = 0

    def test_width(self):
        """Tests the width of the rectangle"""

        sq = Square(10, 15)
        self.assertEqual(sq.width, 10)

        sq.width = 3
        self.assertEqual(sq.width, 3)

        with self.assertRaises(TypeError):
            sq.width = "5"

        with self.assertRaises(TypeError):
            sq.width = None

        with self.assertRaises(TypeError):
            sq.width = 1.1

        with self.assertRaises(ValueError):
            sq.width = -5

        with self.assertRaises(ValueError):
            sq.width = 0

    def test_height(self):
        """Tests the height and width of the square"""

        sq = Square(10)
        self.assertEqual(sq.height, 10)

        sq.height = 3
        self.assertEqual(sq.height, 3)

        sq.height = 7
        self.assertEqual(sq.height, 7)

        with self.assertRaises(TypeError):
            sq.height = "5"

        with self.assertRaises(TypeError):
            sq.height = None

        with self.assertRaises(TypeError):
            sq.height = 1.1

        with self.assertRaises(ValueError):
            sq.width = -5

        with self.assertRaises(ValueError):
            sq.width = 0

    def test_x(self):
        """Tests x of the square"""

        sq = Square(10, x=5)
        self.assertEqual(sq.x, 5)

        sq.x = 0
        self.assertEqual(sq.x, 0)

        with self.assertRaises(TypeError):
            sq.x = "5"

        with self.assertRaises(TypeError):
            sq.x = None

        with self.assertRaises(TypeError):
            sq.x = 1.1

        with self.assertRaises(ValueError):
            sq.x = -5

    def test_y(self):
        """Tests y of the square"""

        sq = Square(10, y=7)
        self.assertEqual(sq.y, 7)

        sq.y = 0
        self.assertEqual(sq.y, 0)

        with self.assertRaises(TypeError):
            sq.y = "5"

        with self.assertRaises(TypeError):
            sq.y = None

        with self.assertRaises(TypeError):
            sq.y = 1.1

        with self.assertRaises(ValueError):
            sq.y = -5

    def test_str(self):
        """Tests the __str__ method"""

        sq = Square(6, 2, 1, 12)
        self.assertEqual(sq.__str__(), "[Square] (12) 2/1 - 6")

        sq = Square(5, 5, 1)
        self.assertEqual(sq.__str__(), "[Square] (1) 5/1 - 5")

        sq = Square(size=7, id=15, y=3, x=4)
        self.assertEqual(sq.__str__(), "[Square] (15) 4/3 - 7")
