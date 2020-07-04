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
        self._last_name = vFunc.valid_alpha_check(lname)  # last name, required: string
        self._first_name = vFunc.valid_alpha_check(fname)  # first name, required: string
        self._street_address = vFunc.valid_alpha_num_check(addStr)  # street address, required: string
        self._city_address = vFunc.valid_alpha_check(addCity)  # city, required: string
        self._state_address = vFunc.state_abbrv_or_full(addState)  # state, required: string
        self._phone_num = vFunc.valid_phone_check(phone)  # phone number, required: 10 digit number
        self._is_salaried = vFunc.valid_bool(salaried)  # if employee is salaried or not, required: True or False
        self._salary = round(vFunc.valid_float_num(salary), 2)  # employee's yearly or weekly pay, required: number
        self.__start_date = vFunc.valid_date(startDate) # employee's start date, required: date


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

    def set_is_salaried(self, salaried):
        self._is_salaried = vFunc.valid_bool(salaried) #if employee is salaried or not, required: True or False

    def set_salary(self, salary):
        self._salary = round(vFunc.valid_float_num(salary), 2) #employee's yearly or weekly pay, required: number

    '''Function to create output string based off an employee class'''
    def display(self):
        if self._is_salaried:
            return (str(self._first_name) + ' ' + str(self._last_name) + '\n' +
                    self._street_address + '\n' +
                    self._city_address + ', ' + self._state_address + '\n' +
                    vFunc.format_phone_num(self._phone_num) + '\n' +
                    'Salaried Employee: $' + str(self._salary) + '/year' + '\n' +
                    'Start Date: ' + str(self.__start_date) + '\n')
        else:
            return (str(self._first_name) + ' ' + str(self._last_name) + '\n' +
                    self._street_address + '\n' +
                    self._city_address + ', ' + self._state_address + '\n' +
                    vFunc.format_phone_num(self._phone_num) + '\n' +
                    'Hourly Employee: $' + str(self._salary) + '/hour' + '\n' +
                    'Start Date: ' + str(self.__start_date) + '\n')

if __name__ == '__main__':
    emp = Employee('Threepwood', 'Guy', '1234 Place', 'Town', 'UT', '1234567890', 'False', 123.45, '01-01-2001')
    print(emp.display())