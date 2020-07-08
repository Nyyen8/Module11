"""
Program: Employee.py
Author: Paul Elsea
Last Modified: 07/3/2020

Defining the Employee class.
"""
from Validation_Utilities import Validation_Functions as vFunc
from class_definitions.Person import Person

class Employee(Person):
    '''Employee class constructor'''
    #Constructor
    def __init__(self, lname, fname, addStr, addCity, addState, phone):
        '''Person object, required:
            # last name, required: string
            # first name, required: string
            # street address, required: string
            # city, required: string
            # state, required: string'''
        super().__init__(lname, fname, addStr, addCity, addState)
        self._phone_num = vFunc.valid_phone_check(phone)  # phone number, required: 10 digit numb


    '''Functions to change individual characteristics of an employee object'''
    def set_last_name(self, lname):
        self._last_name = vFunc.valid_alpha_check(lname) #last name, required: string

    def set_first_name(self, fname):
        self._first_name = vFunc.valid_alpha_check(fname) #first name, required: string

    def set_street_address(self, addStr):
        self._street_address = vFunc.valid_alpha_num_check(addStr) #street address, required: string

    def set_city_address(self, addCity):
        self._city_address = vFunc.valid_alpha_check(addCity) #city, required: string

    def set_state_address(self, addState):
        self._state_address = vFunc.state_abbrv_or_full(addState) #state, required: string

    def set_phone_num(self, phone):
        self._phone_num = vFunc.valid_phone_check(phone) #phone number, required: 10 digit number

    '''Function to create output string based off an employee class'''
    def display(self):
        return (str(self._first_name) + ' ' + str(self._last_name) + '\n' +
                self._street_address + '\n' +
                self._city_address + ', ' + self._state_address + '\n' +
                vFunc.format_phone_num(self._phone_num) + '\n')

if __name__ == '__main__':
    emp = Employee('Threepwood', 'Guy', '1234 Place', 'Town', 'UT', '1234567890')
    print(emp.display())