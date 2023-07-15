#!/usr/bin/python3
"""Test Cases for Rectangle class"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test Class for Rectangle"""

    def setUp(self):
        """method that will be executed before each Test case"""
        Base._Base__nb_objects = 0

    def test_rectangle_without_position(self):
        """Create a Rectangle without setting the position and the id"""
        rec1 = Rectangle(5, 7)
        self.assertEqual(rec1.width, 5)
        self.assertEqual(rec1.height, 7)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec1.y, 0)
        self.assertEqual(rec1.id, 1)

    def test_rectangle_instance(self):
        """Create an instance of Rectangle by setting a value to
        all attributes
        """
        rec1 = Rectangle(2, 4, 0, 0, 1991)
        self.assertEqual(rec1.width, 2)
        self.assertEqual(rec1.height, 4)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec1.y, 0)
        self.assertEqual(rec1.id, 1991)

    def test_multiple_instance(self):
        """Create multiple Rectangles"""
        rec1 = Rectangle(2, 8, 1, 2)
        rec2 = Rectangle(3, 6, 0, 2, 31)
        rec3 = Rectangle(4, 7, 1, 0)
        self.assertEqual(rec1.width, 2)
        self.assertEqual(rec1.height, 8)
        self.assertEqual(rec1.x, 1)
        self.assertEqual(rec1.y, 2)
        self.assertEqual(rec1.id, 1)
        self.assertEqual(rec2.id, 31)
        self.assertEqual(rec3.id, 2)

    def test_access_width(self):
        """Check the access to the private attribute width"""
        with self.assertRaises(AttributeError):
            self.__width

    def test_access_height(self):
        """Check the access to the private attribute height"""
        with self.assertRaises(AttributeError):
            self.__height

    def test_access_x(self):
        """Check the access to the private attribute x"""
        with self.assertRaises(AttributeError):
            self.__x

    def test_access_y(self):
        """Check the access to the private attribute y"""
        with self.assertRaises(AttributeError):
            self.__y

    def test_typeError_raise_width(self):
        """Test raises of TypeError when width value is not integer"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(False, 8, 2, 6)

        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_typeError_raise_height(self):
        """Test raises of TypeError when height value is not integer"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, {"height": 5}, 0, 3)
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_typeError_raise_x(self):
        """Test raises of TypeError when x value is not integer"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, 3, (1, 1), 1)
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_typeError_raise_y(self):
        """Test raises of TypeError when y value is not integer"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, 6, 0, [3, 0])
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_typeError_raise_width_float(self):
        """Test raises of TypeError when width value is a float"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(2.5, 1, 9, 7)
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_valueError_raise_width(self):
        """Test raises of ValueError when width value is less than 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(-1, 2, 6, 7, 33)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_valueError_zero_width(self):
        """Test raises of ValueError when width value is 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(0, 2, 6, 7, 33)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_valueError_raise_height(self):
        """Test raises of ValueError when height value is less than 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(3, -4, 9, 4, 66)
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_valueError_zero_height(self):
        """Test raises of ValueError when height value is 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(3, 0, 9, 4, 66)
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_valueError_raise_x(self):
        """Test raises of ValueError when x value is less than 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(1, 4, -7, 2, 91)
        self.assertEqual(str(ctx.exception), "x must be >= 0")

    def test_valueError_raise_y(self):
        """Test raises of ValueError when y value is less than 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(1, 4, 2, -1, 12)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_typeError_more_args(self):
        """Test instanciate Rectangle with the wrong number of arguments"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 91, 7)

    def test_rectangle_with_no_args(self):
        """Test instanciate Rectangle without args"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_area(self):
        """Test the calcul of the rectangle area"""
        rec = Rectangle(10, 5, 0, 1, 91)
        self.assertEqual(rec.area(), 50)

    def test_area_without_set_position(self):
        """Instanciate Rectangle without setting x and y than
        call area method"""
        rec = Rectangle(5, 3)
        self.assertEqual(rec.area(), 15)

    def test_area_with_change_args(self):
        """Test area with changing width and height"""
        rec = Rectangle(4, 6)
        self.assertEqual(rec.area(), 24)
        rec.width = 5
        self.assertEqual(rec.area(), 30)
        rec.height = 2
        self.assertEqual(rec.area(), 10)
        rec.width = 7
        rec.height = 3
        self.assertEqual(rec.area(), 21)

    def test_area_with_args(self):
        """Call area method with arguments"""
        rec = Rectangle(2, 4, 2, 1)
        with self.assertRaises(TypeError):
            rec.area(2, 5)

    def test_display(self):
        """Test display rectangle method"""
        rec = Rectangle(2, 4, 0, 3, 12)
        expectedOutput = "\n\n\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), expectedOutput)

    def test_display_with_changing(self):
        """Test display rectangle method with changing args"""
        rec = Rectangle(2, 3)
        with patch('sys.stdout', new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), "##\n##\n##\n")
        rec.width = 4
        with patch('sys.stdout', new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), "####\n####\n####\n")
        rec.height = 2
        with patch('sys.stdout', new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), "####\n####\n")
        rec.height = 1
        rec.width = 5
        with patch('sys.stdout', new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), "#####\n")

    def test_display_with_args(self):
        """Test calling display method with arguments"""
        rec = Rectangle(2, 4)
        with self.assertRaises(TypeError):
            rec.display(55)

    def test_str(self):
        """Test calling str method"""
        rec = Rectangle(4, 6, 2, 1, 12)
        expectedResult = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(rec.__str__(), expectedResult)

    def test_str_without_setting_id(self):
        """Test calling str method without setting the id"""
        rec = Rectangle(2, 3, 1, 2)
        expectedResult = "[Rectangle] (1) 1/2 - 2/3"
        self.assertEqual(rec.__str__(), expectedResult)

    def test_str_without_setting_position(self):
        """Test calling str method without setting x, y and id"""
        rec = Rectangle(5, 2)
        expectedResult = "[Rectangle] (1) 0/0 - 5/2"
        self.assertEqual(rec.__str__(), expectedResult)

    def test_str_with_changes(self):
        """Test calling str method with changing attributes value"""
        rec = Rectangle(3, 4, 1, 7, 91)
        self.assertEqual(rec.__str__(), "[Rectangle] (91) 1/7 - 3/4")
        rec.x = 3
        rec.y = 5
        self.assertEqual(rec.__str__(), "[Rectangle] (91) 3/5 - 3/4")
        rec.width = 6
        rec.height = 5
        self.assertEqual(rec.__str__(), "[Rectangle] (91) 3/5 - 6/5")
        rec.x = 0
        rec.height = 9
        self.assertEqual(rec.__str__(), "[Rectangle] (91) 0/5 - 6/9")

    def test_str_with_args(self):
        """Test calling str method with arguments"""
        rec = Rectangle(3, 4, 1, 0, 91)
        with self.assertRaises(TypeError):
            rec.__str__(2, 7)

    def test_str_multiple_rectangle(self):
        """Test calling str method with multiple
        Rectangles instances
        """
        rec1 = Rectangle(3, 5)
        rec2 = Rectangle(2, 7, 1, 3)
        rec3 = Rectangle(10, 2, 1, 4, 91)
        self.assertEqual(rec1.__str__(), "[Rectangle] (1) 0/0 - 3/5")
        self.assertEqual(rec2.__str__(), "[Rectangle] (2) 1/3 - 2/7")
        self.assertEqual(rec3.__str__(), "[Rectangle] (91) 1/4 - 10/2")

    def test_display_with_handle_position(self):
        """Test display method with handling x and y"""
        rec = Rectangle(5, 2, 4, 2, 3)
        rec1 = Rectangle(7, 3, 2, 0)
        rec2 = Rectangle(10, 2, 0, 4, 91)
        with patch("sys.stdout", new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), "\n\n    #####\n    #####\n")
        with patch("sys.stdout", new=StringIO()) as out:
            rec1.display()
            self.assertEqual(out.getvalue(),
                             "  #######\n  #######\n  #######\n")
        with patch("sys.stdout", new=StringIO()) as out:
            rec2.display()
            self.assertEqual(out.getvalue(),
                             "\n\n\n\n##########\n##########\n")