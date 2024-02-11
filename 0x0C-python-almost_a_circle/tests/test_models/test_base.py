#!/usr/bin/python3

"""This module has TestBase class to test the Base class"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


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

    def test_save_to_file(self):
        """Tests save_to_file function"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        self.assertTrue(os.path.isfile("Rectangle.json"))

        with open("Rectangle.json", "r") as file1:
            file_list1 = file1.read()

        json_dictionary1 = Rectangle.to_json_string([r1.to_dictionary(),
                                                    r2.to_dictionary()])
        self.assertEqual(json_dictionary1, file_list1)

        sq1 = Square(10, 2, 8)
        sq2 = Square(2)
        Square.save_to_file([sq1, sq2])

        self.assertTrue(os.path.isfile("Square.json"))

        with open("Square.json", "r") as file2:
            file_list2 = file2.read()

        json_dictionary2 = Square.to_json_string([sq1.to_dictionary(),
                                                  sq2.to_dictionary()])
        self.assertEqual(json_dictionary2, file_list2)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file3:
            self.assertEqual(file3.read(), "[]")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file3:
            self.assertEqual(file3.read(), "[]")

    def test_from_json_string(self):
        """Tests from_json_string function"""

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_input, list_output)

        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)

        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_input, list_output)

        self.assertEqual(Rectangle.from_json_string(""), [])
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string("[{}, {}]"), [{}, {}])
        self.assertEqual(Rectangle.from_json_string("[]"), [])
        self.assertEqual(
            Rectangle.from_json_string('[{"age": 35}, {"country": "Egypt"}]'),
            [{"age": 35}, {"country": "Egypt"}])
