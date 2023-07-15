#!/usr/bin/python3
"""Unittest for Base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Definition of test class of Base"""

    def setUp(self):
        """Method that execute before each Test"""
        Base._Base__nb_objects = 0

    def test_id_None(self):
        """Test id Base attribute with None initialization"""
        baseTest = Base()
        self.assertEqual(baseTest.id, 1)

    def test_id_with_value(self):
        """Test id Base attribute with value"""
        baseTest = Base(5)
        self.assertEqual(baseTest.id, 5)

    def test_access_nb_objects(self):
        """Test access to the private class attribute __nb_objects"""
        baseTest = Base()
        with self.assertRaises(AttributeError):
            print(baseTest.__nb_objects)

    def test_multiple_instance(self):
        """Test multiple instances without setting id value"""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_mix_instances(self):
        """Test with multiple mix Base instances"""
        base1 = Base()
        base2 = Base(91)
        base3 = Base()
        base4 = Base(99)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 91)
        self.assertEqual(base3.id, 2)
        self.assertEqual(base4.id, 99)

    def test_multiple_args(self):
        """Test instanciate Base with multiple args"""
        with self.assertRaises(TypeError):
            baseTest = Base(5, 8)

    def test_with_string_val(self):
        """Test instanciate Base with a String value"""
        baseTest = Base("1991")
        self.assertEqual(baseTest.id, "1991")
