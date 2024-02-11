#!/usr/bin/python3

"""This module has TestBase class to test the Base class"""

from models.base import Base
from models.rectangle import Rectangle
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

        b5 = Base()
        self.assertEqual(b5.id, 5)
        b5.id = 15
        self.assertEqual(b5.id, 15)

    def test_to_json_string(self):
        """Tests to_json_string function"""

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(type(dictionary), dict)

        json_dictionary1 = Base.to_json_string([dictionary])

        self.assertEqual(json_dictionary1, str([dictionary]).replace("'", '"'))
        self.assertEqual(type(json_dictionary1), str)

        json_dictionary2 = Base.to_json_string([])
        self.assertEqual(type(json_dictionary2), str)
        self.assertEqual(json_dictionary2, "[]")

        json_dictionary3 = Base.to_json_string(None)
        self.assertEqual(type(json_dictionary3), str)
        self.assertEqual(json_dictionary3, '[]')

        json_dictionary4 = Base.to_json_string([{}, {}])
        self.assertEqual(json_dictionary4, "[{}, {}]")

        json_dictionary5 = Base.to_json_string([{"age": 30},
                                                {"country": "Egypt"}])
        self.assertEqual(json_dictionary5,
                         '[{"age": 30}, {"country": "Egypt"}]')

        with self.assertRaises(TypeError):
            Base.to_json_string()
