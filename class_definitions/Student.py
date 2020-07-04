"""
Program: Student.py
Author: Paul Elsea
Last Modified: 07/3/2020

Defining the Student class.
"""

from Validation_Utilities import Validation_Functions as vFunc

class Student:
    '''Student class constructor'''
    #Constructor
    def __init__(self, lname, fname, major, gpa=0.0):
        self._last_name = vFunc.valid_alpha_check(lname) #last name, required: string
        self._first_name = vFunc.valid_alpha_check(fname) #first name, required: string
        self._major = vFunc.valid_alpha_check(major)  # first name, required: string
        self._gpa = gpa  # student's GPA, optional: int/float

    def __str__(self):
        return self._last_name + ', ' + self._first_name + ' is majoring in ' + self._major + ' with a GPA of ' + str(self._gpa)

if __name__ == '__main__':
    bob_student = Student('Bob', 'Billy', 'Billy bobbing', 4.0)
    print(str(bob_student))
