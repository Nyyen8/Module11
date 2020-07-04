import unittest
from class_definitions import Student as std

class StudentTestCases(unittest.TestCase):
    def setUp(self):
       self.Student = std.Student('Bob', 'Billy', 'Billy bobbing', 4.0)

    def tearDown(self):
       del self.Student


    def test_object_created_required_attributes(self):
        self.assertEqual(self.Student._last_name, 'Bob')
        self.assertEqual(self.Student._first_name, 'Billy')
        self.assertEqual(self.Student._major, 'Billy bobbing')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.Student._last_name, 'Bob')
        self.assertEqual(self.Student._first_name, 'Billy')
        self.assertEqual(self.Student._major, 'Billy bobbing')
        self.assertEqual(self.Student._gpa, 4.0)

    def test_student_str(self):
        self.assertEqual(str(self.Student), 'Bob, Billy is majoring in Billy bobbing with a GPA of 4.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            test = std.Student('0000', 'Billy', 'Billy bobbing')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            test = std.Student('Bob', '0000', 'Billy bobbing')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            test = std.Student('Bob', 'Billy', '0000')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            test = std.Student('Bob', 'Billy', 'Billy bobbing', 'abcd')
            test = std.Student('Bob', 'Billy', 'Billy bobbing', 5.0)
            test = std.Student('Bob', 'Billy', 'Billy bobbing', -1)


if __name__ == '__main__':
    unittest.main()
