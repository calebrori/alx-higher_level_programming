#!/usr/bin/python3
"""Defines unittests for models/rectangle.py"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_instantiation(self):
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(1, r.id)
        self.assertEqual(10, r.width)
        self.assertEqual(2, r.height)
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)

        r = Rectangle(2, 10)
        self.assertEqual(2, r.id)

    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(1)

        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(TypeError):
            Rectangle(5, 5, 0, 0, 1).__width

        with self.assertRaises(AttributeError):
            r = Rectangle(5, 7, 7, 5, 1)
            r.__width = 10

    def test_area(self):
        r = Rectangle(10, 2)
        self.assertEqual(20, r.area())

        r.width = 5
        r.height = 4
        self.assertEqual(20, r.area())

    def test_str_method(self):
        r = Rectangle(4, 6)
        self.assertEqual("[Rectangle] (1) 0/0 - 4/6", str(r))

        r.width = 5
        r.height = 7
        self.assertEqual("[Rectangle] (1) 0/0 - 5/7", str(r))

    def test_display_method(self):
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        self.assertEqual(expected_output, r.display())

        r = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        self.assertEqual(expected_output, r.display())

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

        with self.assertRaises(TypeError):
            r.update(89, "invalid")

        with self.assertRaises(ValueError):
            r.update(89, 0)

        with self.assertRaises(ValueError):
            r.update(89, -5)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

        r.update(id=89, x=1, height=2)
        self.assertEqual("[Rectangle] (89) 1/10 - 2/10", str(r))

        with self.assertRaises(TypeError):
            r.update(width="invalid")

        with self.assertRaises(ValueError):
            r.update(height=0)

        with self.assertRaises(ValueError):
            r.update(height=-5)


if __name__ == "__main__":
    unittest.main()
