"""
Program: test_student.py
Author: Paul Elsea
Last Modified: 07/4/2020

Tests to verify functions used in Student.py.
"""

import unittest
from class_definitions import Student as std

class StudentTestCases(unittest.TestCase):
    '''Method to set up a test object'''
    def setUp(self):
       self.Student = std.Student('Bob', 'Billy', 'Billy bobbing', 4.0)

    '''Method to delete a test object'''
    def tearDown(self):
       del self.Student

    '''Test to ensure attributes are being properly applied, and optional attribute not required'''
    def test_object_created_required_attributes(self):
        self.assertEqual(self.Student._last_name, 'Bob')
        self.assertEqual(self.Student._first_name, 'Billy')
        self.assertEqual(self.Student._major, 'Billy bobbing')

    '''Test to ensure attributes are being properly applied and optional attribute also applied correctly'''
    def test_object_created_all_attributes(self):
        self.assertEqual(self.Student._last_name, 'Bob')
        self.assertEqual(self.Student._first_name, 'Billy')
        self.assertEqual(self.Student._major, 'Billy bobbing')
        self.assertEqual(self.Student._gpa, 4.0)

    '''Test to ensure str() returns proper string'''
    def test_student_str(self):
        self.assertEqual(str(self.Student), 'Bob, Billy is majoring in Billy bobbing with a GPA of 4.0')

    '''Test to ensure ValueError exception is thrown with incorrect lname input'''
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            test = std.Student('0000', 'Billy', 'Billy bobbing')

    '''Test to ensure ValueError exception is thrown with incorrect fname input'''
    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            test = std.Student('Bob', '0000', 'Billy bobbing')

    '''Test to ensure ValueError exception is thrown with incorrect major input'''
    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            test = std.Student('Bob', 'Billy', '0000')

    '''Test to ensure ValueError exception is thrown with incorrect GPA input'''
    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            test = std.Student('Bob', 'Billy', 'Billy bobbing', 'abcd')
            test = std.Student('Bob', 'Billy', 'Billy bobbing', 5.0)
            test = std.Student('Bob', 'Billy', 'Billy bobbing', -1)


if __name__ == '__main__':
    unittest.main()
