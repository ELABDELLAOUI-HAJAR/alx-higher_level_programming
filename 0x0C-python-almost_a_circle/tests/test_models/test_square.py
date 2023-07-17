#!/usr/bin/python3
"""Define Test class for Square class"""
import unittest
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO


class TestSquare(unittest.TestCase):
    """Definition of the Test square class"""

    def setUp(self):
        """method that execute before each test case"""
        Base._Base__nb_objects = 0

    def test_square(self):
        """Test instanciate a square and calling area,
        display methods
        """
        square = Square(2, 1, 3, 98)
        self.assertEqual(square.__str__(), "[Square] (98) 1/3 - 2")
        self.assertEqual(square.area(), 4)
        with patch("sys.stdout", new=StringIO()) as out:
            square.display()
            self.assertEqual(out.getvalue(), "\n\n\n ##\n ##\n")

    def test_square_size_zero(self):
        """Test Square with size equal to 0"""
        with self.assertRaises(ValueError) as ctx:
            square = Square(0)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_square_size_negative(self):
        """Test Square with negative value of size"""
        with self.assertRaises(ValueError) as ctx:
            square = Square(-9)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_square_size_wrong_type(self):
        """Test Square with a wrong type of size"""
        with self.assertRaises(TypeError) as ctx:
            square = Square(9.75)
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_square_x_wrong_type(self):
        """Test Square with a wrong type of x"""
        with self.assertRaises(TypeError) as ctx:
            square = Square(2, (7, 'H'))
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_square_negative_x(self):
        """Test Square with a negative value of x"""
        with self.assertRaises(ValueError) as ctx:
            square = Square(2, -1)
        self.assertEqual(str(ctx.exception), "x must be >= 0")

    def test_square_y_wrong_type(self):
        """Test Square with a wrong type of y"""
        with self.assertRaises(TypeError) as ctx:
            square = Square(2, 3, False)
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_square_negative_y(self):
        """Test Square with a negative value of y"""
        with self.assertRaises(ValueError) as ctx:
            square = Square(2, 3, -5)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_square_without_setting_id(self):
        """Test Square without setting the id"""
        square = Square(2, 1, 0)
        self.assertEqual(square.__str__(), "[Square] (1) 1/0 - 2")
        with patch("sys.stdout", new=StringIO()) as out:
            square.display()
            self.assertEqual(out.getvalue(), " ##\n ##\n")

    def test_square_extra_args(self):
        """Test Square with extrat arguments"""
        with self.assertRaises(TypeError):
            square = Square(2, 1, 0, 41, 8)

    def test_square_get_size(self):
        """Test the getter of square size"""
        square = Square(2, 1, 0)
        self.assertEqual(square.size, 2)

    def test_square_setter_size(self):
        """Test the setter of square size"""
        square = Square(2, 1, 1)
        self.assertEqual(square.size, 2)
        square.size = 6
        self.assertEqual(square.size, 6)
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)

    def test_square_set_zero_size(self):
        """Test the setter of square size by passing 0 value"""
        square = Square(2, 1, 1)
        with self.assertRaises(ValueError) as ctx:
            square.size = 0
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_square_set_negative_size(self):
        """Test the setter of square size by passing a negative value"""
        square = Square(2, 1, 1)
        with self.assertRaises(ValueError) as ctx:
            square.size = -5
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_square_set_size_wrong_type(self):
        """Test the setter of square size by passing a wrong type"""
        square = Square(2, 1, 1, 23)
        with self.assertRaises(TypeError) as ctx:
            square.size = 9.26
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_update_args_id(self):
        """Test updating id with update method"""
        square = Square(3)
        self.assertEqual(square.__str__(), "[Square] (1) 0/0 - 3")
        square.update(11)
        self.assertEqual(square.__str__(), "[Square] (11) 0/0 - 3")

    def test_update_args_size(self):
        """Test updating size by using update method"""
        square = Square(3)
        self.assertEqual(square.__str__(), "[Square] (1) 0/0 - 3")
        square.update(11, 6)
        self.assertEqual(square.__str__(), "[Square] (11) 0/0 - 6")

    def test_update_args_x(self):
        """Test updateing x by calling update method"""
        square = Square(3)
        self.assertEqual(square.__str__(), "[Square] (1) 0/0 - 3")
        square.update(11, 6, 2)
        self.assertEqual(square.__str__(), "[Square] (11) 2/0 - 6")

    def test_update_args_y(self):
        """Test updating y by calling update method"""
        square = Square(3, 5, 6, 12)
        self.assertEqual(square.__str__(), "[Square] (12) 5/6 - 3")
        square.update(11, 6, 2, 9)
        self.assertEqual(square.__str__(), "[Square] (11) 2/9 - 6")

    def test_update_with_args_kwargs(self):
        """Test calling update method with args and kwargs values"""
        square = Square(3, 5, 6, 12)
        self.assertEqual(square.__str__(), "[Square] (12) 5/6 - 3")
        square.update(10, 2, 8, 9, size=5, id=87)
        self.assertEqual(square.__str__(), "[Square] (10) 8/9 - 2")

    def test_update_with_kwargs(self):
        """Test calling update method by passing kwargs"""
        square = Square(3, 0, 4, 15)
        self.assertEqual(square.__str__(), "[Square] (15) 0/4 - 3")
        square.update(id=20, x=3, size=7, y=9)
        self.assertEqual(square.__str__(), "[Square] (20) 3/9 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary method of square"""
        square = Square(10, 2, 1)
        dic = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(square.to_dictionary(), dic)

    def test_to_dictionary_min(self):
        """Test to_dictionary method for the minimum instance
        creation
        """
        square = Square(6)
        dic = {'id': 1, 'x': 0, 'size': 6, 'y': 0}
        self.assertDictEqual(square.to_dictionary(), dic)

    def test_type_return_dict_square(self):
        """Test to check the type of the returned value of
        to_dictionary method of square
        """
        square = Square(10, 2, 1)
        self.assertIs(type(square.to_dictionary()), dict)

    def test_to_dictionary_with_manip(self):
        """Test to_dictionary method with some manipulations"""
        s1 = Square(10, 2, 1)
        dic = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(s1.to_dictionary(), dic)
        s2 = Square(1, 1)
        dic2 = {'id': 2, 'x': 1, 'size': 1, 'y': 0}
        self.assertDictEqual(s2.to_dictionary(), dic2)
        s2.update(**s1.to_dictionary())
        self.assertDictEqual(s2.to_dictionary(), dic)
        self.assertFalse(s1 == s2)

    def test_to_save_to_file_square(self):
        """Test save_to_file class method"""
        s1 = Square(3)
        s2 = Square(6, 1, 5, 91)
        dic1 = s1.to_dictionary()
        dic2 = s2.to_dictionary()
        Square.save_to_file([s1, s2])
        expected = "[{}, {}]\n".format(dic1, dic2)
        with patch("sys.stdout", new=StringIO()) as out:
            with open("Square.json", "r") as file:
                print(file.read())
            self.assertEqual(out.getvalue(), expected.replace("'", "\""))

    def test_square_save_to_file_None(self):
        """Test save_to_file method with None arg"""
        Square.save_to_file(None)
        with patch("sys.stdout", new=StringIO()) as out:
            with open("Square.json", "r") as file:
                print(file.read())
            self.assertEqual(out.getvalue(), "[]\n")

    def test_square_save_to_file_empty(self):
        """Test save_to_file method with an empty list arg"""
        Square.save_to_file([])
        with patch("sys.stdout", new=StringIO()) as out:
            with open("Square.json", "r") as file:
                print(file.read())
            self.assertEqual(out.getvalue(), "[]\n")

    def test_square_to_json_string(self):
        """Test to_json_string method for square class"""
        s1 = Square(3)
        s2 = Square(6, 1, 5, 91)
        dic1 = s1.to_dictionary()
        dic2 = s2.to_dictionary()
        json_str = Square.to_json_string([dic1, dic2])
        expected = "[{}, {}]".format(dic1, dic2)
        self.assertEqual(json_str, expected.replace("'", "\""))

    def test_square_to_json_string_None(self):
        """Test to_json_string method with None arg"""
        json_str = Square.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_square_to_json_string_empty(self):
        """Test to_json_string method with empty list arg"""
        json_str = Square.to_json_string([])
        self.assertEqual(json_str, "[]")
