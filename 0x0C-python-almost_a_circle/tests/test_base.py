#!/usr/bin/python3

"""This module has TestBase class to test the Base class"""

from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """This class is for testing Base class attributes and functions"""

    def test_id(self):
        """Tests the increment of the id attribute in the Base class"""

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b1 = Base()
        self.assertEqual(b1.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 4)
