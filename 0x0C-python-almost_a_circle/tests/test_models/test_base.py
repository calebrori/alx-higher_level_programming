#!/usr/bin/python3
"""Defines unittests for base.py.

import os
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestModels(unittest.TestCase):
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_rectangle_creation(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        self.assertEqual(str(r1), "[Rectangle] (7) 1/2 - 3/5")

    def test_square_creation(self):
        s1 = Square(10, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (4) 2/3 - 10")

    def test_unique_id_assignment(self):
        r1 = Rectangle(3, 5)
        r2 = Rectangle(2, 4)
        self.assertEqual(r2.id, r1.id + 1)

    def test_to_json_string_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 6)
        json_string = Rectangle.to_json_string([r.to_dictionary()])
        self.assertTrue(isinstance(json_string, str))

    def test_to_json_string_square(self):
        s = Square(10, 2, 3, 4)
        json_string = Square.to_json_string([s.to_dictionary()])
        self.assertTrue(isinstance(json_string, str))

    def test_from_json_string_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 6)
        json_string = Rectangle.to_json_string([r.to_dictionary()])
        list_objs = Rectangle.from_json_string(json_string)
        self.assertEqual(len(list_objs), 1)
        self.assertEqual(str(r), str(list_objs[0]))

    def test_from_json_string_square(self):
        s = Square(10, 2, 3, 4)
        json_string = Square.to_json_string([s.to_dictionary()])
        list_objs = Square.from_json_string(json_string)
        self.assertEqual(len(list_objs), 1)
        self.assertEqual(str(s), str(list_objs[0]))

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))

    def test_create_square(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_save_to_file_square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))
        self.assertEqual(str(s2), str(list_squares_output[1]))


if __name__ == "__main__":
    unittest.main()
