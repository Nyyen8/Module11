import unittest
from class_definitions import Student as std

class StudentTestCases(unittest.TestCase):
    def setUp(self):
       self.Student = std.Student('Bob', 'Billy', 'Billy bobbing', 4.0)

    def tearDown(self):
       del self.Student



    def test_object_created_required_attributes(self):
        self.assertEqual(True, False)

    def test_object_created_all_attributes(self):
        self.assertEqual(True, False)

    def test_test_object_created_required_attributes(self):
        self.assertEqual(True, False)

    def test_student_str(self):
        self.assertEqual(True, False)

    def test_object_not_created_error_last_name(self):
        self.assertEqual(True, False)

    def test_object_not_created_error_first_name(self):
        self.assertEqual(True, False)

    def test_object_not_created_error_major(self):
        self.assertEqual(True, False)

    def test_object_not_created_error_gpa(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
