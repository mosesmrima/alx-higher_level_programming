#!/usr/bin/python3

""" This module contains the test suite for the models.base module
    Class tested: Base
    Methods tested:
                   Base.__init__
                   Base.to_json_string
                   Base.save_to_file
                   Base.from_json_string
                   Base.create
                   Base.load_from_file
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_init(unittest.TestCase):
    """test the Base class instansiaction"""

    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        self.assertEqual(b.id, b1.id - 1)

    def test_set_id(self):
        b = Base(45)
        self.assertEqual(b.id, 45)


class TestBase_to_json_string(unittest.TestCase):
    def test_to_json_string_with_None(self):
        b = Base()
        self.assertEqual("[]", b.to_json_string(None))

    def test_to_json_string_with_empty_list(self):
        b = Base()
        self.assertEqual("[]", b.to_json_string([]))

    def test_to_json_string_with_valid_param(self):
        b = Base()
        l = [{"fname": "John", "lname": "Doe"}, {"fname": "Bob"}]
        self.assertTrue(type(l), list)
        self.assertTrue(type(b.to_json_string(l)), str)


class TestBase_from_json_string(unittest.TestCase):
    def test_from_json_string_with_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_with_None(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_with_valid_param(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4},
            {"id": 7, "width": 1, "height": 7},
        ]
        self.assertTrue(type(list_input), list)
        json_list_input = Rectangle.to_json_string(list_input)
        self.assertTrue(type(json_list_input), str)
        self.assertTrue(type(Base.from_json_string(json_list_input)), list)


class TestBase_load_from_file(unittest.TestCase):
    """test the load_from_file of Base"""

    @classmethod
    def tearDown(self):
        """cleanup created files after tests"""
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_load_from_file_square(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        out = Square.load_from_file()
        self.assertEqual(str(s), str(out[0]))

    def test_load_from_file_square_check_type(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        out = Square.load_from_file()
        self.assertTrue(type(out[0]), "Square")

    def test_load_from_file_rectangle(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        out = Rectangle.load_from_file()
        self.assertEqual(str(r), str(out[0]))

    def test_load_from_file_rectangle_check_type(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        out = Rectangle.load_from_file()
        self.assertTrue(type(out[0]), "Rectangle")


if __name__ == "__main__":
    unittest.main()
