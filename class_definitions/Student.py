"""
Program: Student.py
Author: Paul Elsea
Last Modified: 07/4/2020

Defining the Student class.
"""

from Validation_Utilities import Validation_Functions as vFunc
from class_definitions.Person import Person

class Student(Person):
    '''Student class constructor'''
    #Constructor
    def __init__(self, student_id, person_ob_lname, person_ob_fname, major='Computer Science', gpa=0.0):
        '''Person object, required:
            # last name, required: string
            # first name, required: string'''
        super().__init__(person_ob_lname, person_ob_fname)
        self._student_id = vFunc.valid_id_check(student_id)  # student ID #, required: 9 digit int
        self._major = vFunc.valid_name_check(major)  # major, optional: string
        self._gpa = vFunc.valid_gpa_check(gpa)  # student's GPA, optional: int/float

    '''Function to change the major of a student object'''
    def change_major(self, major):
        self._major = vFunc.valid_name_check(major)  # major, required: string

    '''Function to change the gpa of a student object'''
    def change_gpa(self, gpa):
        self._gpa = vFunc.valid_gpa_check(gpa)  # student's GPA, required: int/float

    '''Returns string based off of student object attributes'''
    def display(self):
        return self._last_name + ', ' + self._first_name + ': ' + '(' + str(self._student_id) + ')' + ' ' + \
               self._major + ' with a GPA of' + ' ' + str(self._gpa)

if __name__ == '__main__':
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student
