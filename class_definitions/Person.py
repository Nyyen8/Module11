"""
Program: Person.py
Author: Paul Elsea
Last Modified: 07/8/2020

Defining the Person class.
"""

from Validation_Utilities import Validation_Functions as vFunc
from class_definitions.Address import Address

class Person(Address):
    '''Person class constructor'''
    #Constructor
    def __init__(self, lname, fname, addStr, addCity, addState):
        self._last_name = vFunc.valid_name_check(lname)  # last name, required: string
        self._first_name = vFunc.valid_name_check(fname)  # first name, required: string
        '''Address object, required:
            # street address, required: string
            # city, required: string
            # state, required: string'''
        super().__init__(addStr, addCity, addState)

    '''Returns string based off of student object attributes'''
    def display(self):
        return 'This is a person named ' + self._first_name + ' ' + self._last_name + '\n' +\
        self._street_address + '\n' + self._city_address + ', ' + self._state_address + '\n'

if __name__ == '__main__':
    new_person = Person('Vogel', 'Birdy', '1234 Place', 'Town', 'UT')
    print(new_person.display())
