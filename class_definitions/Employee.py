"""
Program: Employee.py
Author: Paul Elsea
Last Modified: 07/3/2020

Defining the Employee class.
"""
from Validation_Utilities import Validation_Functions as vFunc

class Employee:
    '''Employee class constructor'''
    #Constructor
    def __init__(self, lname, fname, addStr, addCity, addState,
                 phone, salaried, salary, startDate):
        self._last_name = vFunc.valid_alpha_check(lname)
        self._first_name = vFunc.valid_alpha_check(fname)
        self._street_address = vFunc.valid_alpha_num_check(addStr)
        self._city_address = vFunc.valid_alpha_check(addCity)
        self._state_address = vFunc.state_abbrv_or_full(addState)
        self._phone_num = vFunc.valid_phone_check(phone)
        self._is_salaried = vFunc.valid_bool(salaried)
        self._salary = round(vFunc.valid_float_num(salary), 2)
        self.__start_date = vFunc.valid_date(startDate)


    '''Functions to change individual characteristics of an employee object'''
    def set_last_name(self, lname):
        self._last_name = vFunc.valid_alpha_check(lname)

    def set_first_name(self, fname):
        self._first_name = vFunc.valid_alpha_check(fname)

    def set_street_address(self, addStr):
        self._street_address = vFunc.valid_alpha_num_check(addStr)

    def set_city_address(self, addCity):
        self._city_address = vFunc.valid_alpha_check(addCity)

    def set_state_address(self, addState):
        self._state_address = vFunc.state_abbrv_or_full(addState)

    def set_phone_num(self, phone):
        self._phone_num = vFunc.valid_phone_check(phone)

    def set_is_salaried(self, salaried):
        self.is_salaried = vFunc.valid_bool(salaried)

    def set_salary(self, salary):
        self.salary = round(vFunc.valid_float_num(salary), 2)

    '''Function to create output string based off an employee class'''
    def display(self):
        if self._is_salaried:
            return str(str(self.first_name) + ' ' + str(self.last_name) + '\n' +
                    self.street_address + '\n' +
                    self.city_address + ', ' + self.state_address + '\n' +
                    str(self.phone_num) + '\n' +
                    'Salaried Employee: $' + str(self.salary) + '/year' + '\n' +
                    'Start Date: ' + str(self.start_date) + '\n')
        else:
            return str(str(self.first_name) + ' ' + str(self.last_name) + '\n' +
                    self.street_address + '\n' +
                    self.city_address + ', ' + self.state_address + '\n' +
                    str(self.phone_num) + '\n' +
                    'Hourly Employee: $' + str(self.salary) + '/hour' + '\n' +
                    'Start Date: ' + str(self.start_date) + '\n')

#Driver Example
emp = Employee('Threepwood', 'Guy', '1234 Place', 'Town', 'UT', '1234567890', 'False', '123.45', '01-01-2001')
print(emp.display())
del emp