#!/usr/bin/python3

"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class test max_integer function"""

    def test_int_list(self):
        """Test max_integer function with regular list of intgeres"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
        self.assertEqual(max_integer((-1, -25, -100, -5)), -1)
        self.assertEqual(max_integer((1, 1.5, 1.75, 1.80)), 1.80)
        self.assertEqual(max_integer((95, 95, 95, 95)), 95)

    def test_empty(self):
        """Test max_integer function with empty list"""

        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_str(self):
        """Test max_integer function with a regular list of strings"""

        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer(["1", "2", "3", "4"]), "4")

    def test_multiple_types(self):
        """Test max_integer function with a list of multiple types"""
        self.assertRaises(TypeError, max_integer, ["1", 2, 3])

    def test_tuplel(self):
        """Test max_integer function with regular a tuple of intgeres"""
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

    def test_not_iterable(self):
        """Test max_integer function with none iterable values"""

        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, None)

    def test_dict(self):
        """Test max_integer function with regular a dict"""

        self.assertRaises(KeyError, max_integer, {1: 2, 5: 3})
