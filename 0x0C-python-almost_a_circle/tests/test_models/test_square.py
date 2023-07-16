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
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_square_size_negative(self):
        """Test Square with negative value of size"""
        with self.assertRaises(ValueError):
            square = Square(-9)

    def test_square_size_wrong_type(self):
        """Test Square with a wrong type of size"""
        with self.assertRaises(TypeError):
            square = Square(9.75)

    def test_square_x_wrong_type(self):
        """Test Square with a wrong type of x"""
        with self.assertRaises(TypeError):
            square = Square(2, (7, 'H'))

    def test_square_negative_x(self):
        """Test Square with a negative value of x"""
        with self.assertRaises(ValueError):
            square = Square(2, -1)

    def test_square_y_wrong_type(self):
        """Test Square with a wrong type of y"""
        with self.assertRaises(TypeError):
            square = Square(2, 3, False)

    def test_square_negative_y(self):
        """Test Square with a negative value of y"""
        with self.assertRaises(ValueError):
            square = Square(2, 3, -5)

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
