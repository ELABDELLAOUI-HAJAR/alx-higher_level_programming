#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Definition of TestMaxInteger that contain
        testCases for max_integer function
    """
    def test_empty_list(self):
        """Test the case of empty list"""
        self.assertEqual(max_integer([]), None)

    def test_max_beginning(self):
        """Test the case where the max is the 
        first element of the list"""
        max_begin_list = [15, 3, 0, 9, 1]
        self.assertEqual(max_integer(max_begin_list), 15)

    def test_ordered_list(self):
        """Test the case of ordered list"""
        ordered_list = [2, 4, 6, 8, 10]
        self.assertEqual(max_integer(ordered_list), 10)

    def test_unordered_list(self):
        """Test the case of unordered list"""
        unordered_list = [-5, 4, -25, 42, 0, 33]
        self.assertEqual(max_integer(unordered_list), 42)

    def test_string(self):
        """Test the case of string param (list of characters)"""
        string = "SHAHRAZAD"
        self.assertEqual(max_integer(string), 'Z')

    def test_string_list(self):
        """Test the case a list of strings"""
        string_list = ["Begin", "Hello", "Hajar", "Sea"]
        self.assertEqual(max_integer(string_list), "Sea")

    def test_float_list(self):
        """Test the case where the elements of the list
            are floats
        """
        float_list = [3.5, -0.5, 4.15, -9.87, 0.99]
        self.assertEqual(max_integer(float_list), 4.15)

    def test_float_int_list(self):
        """Test the case where the elements of the list
            are mixte float and int
        """
        int_float_list = [5, -0.3, 14, 2, 5.5, 6.75]
        self.assertEqual(max_integer(int_float_list), 14)

    def test_empty_string(self):
        """Test the case of empty string"""
        self.assertEqual(max_integer(""), None)

    def test_one_list(self):
        """Test the case of a list with single element"""
        single_elmt_list = [27]
        self.assertEqual(max_integer(single_elmt_list), 27)


if __name__ == "__main__":
    unittest.main()

