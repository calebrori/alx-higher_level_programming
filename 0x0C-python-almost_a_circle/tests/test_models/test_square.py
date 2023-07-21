import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    def test_is_base_and_square(self):
        self.assertIsInstance(Square(5), Square)

    def test_no_args_raises_error(self):
        with self.assertRaises(TypeError):
            Square()

    def test_correct_id_assignment(self):
        s1 = Square(5)
        s2 = Square(3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_attributes_assignment(self):
        s1 = Square(5, 4)
        s2 = Square(4, 5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_more_than_four_args_raises_error(self):
        with self.assertRaises(TypeError):
            Square(6, 7, 8, 9, 1)

    def test_private_attribute_raises_error(self):
        with self.assertRaises(AttributeError):
            print(Square(7, 8, 1, 4).__size)

    def test_size_getter(self):
        self.assertEqual(8, Square(4, 1, 8, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_area(self):
        s = Square(10)
        self.assertEqual(100, s.area())

    def test_str_method(self):
        s = Square(4, 1, 9, 2)
        self.assertEqual("[Square] (2) 1/9 - 4", str(s))

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1, size=5, x=2, y=3)
        self.assertEqual("[Square] (1) 2/3 - 5", str(s))

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())


if __name__ == "__main__":
    unittest.main()
