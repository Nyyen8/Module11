"""
Program: SalariedEmployee.py
Author: Paul Elsea
Last Modified: 07/8/2020

Defining the SalariedEmployee class.
"""
from Validation_Utilities import Validation_Functions as vFunc
from class_definitions.Employee import Employee

class SalariedEmployee(Employee):
    '''SalariedEmployee class constructor'''
    #Constructor
    def __init__(self, lname, fname, addStr, addCity, addState, phone, startDate, salary):
        '''Employee object, required:
            # last name, required: string
            # first name, required: string
            # street address, required: string
            # city, required: string
            # state, required: string
            # phone number, required: 10 digit number'''
        super().__init__(lname, fname, addStr, addCity, addState, phone)
        self._salary = round(vFunc.valid_float_num(salary), 2)  # employee's yearly or weekly pay, required: number
        self.__start_date = vFunc.valid_date(startDate)  # employee's start date, required: date


    '''Functions to change individual characteristics of an employee object'''
    def set_salary(self, salary):
        self._salary = round(vFunc.valid_float_num(salary), 2) #employee's yearly or weekly pay, required: number

    def set_start_date(self, startDate):
        self._start_date = vFunc.valid_date(startDate)  # employee's start date, required: date

    '''Function to raise salary of SalariedEmployee object'''
    def give_raise(self, raise_amount):
        self._salary = round(vFunc.valid_float_num(raise_amount), 2)  # employee's yearly pay, required: int/float

    '''Function to create output string based off an employee class'''
    def display(self):
        return (str(self._first_name) + ' ' + str(self._last_name) + '\n' +
                self._street_address + '\n' +
                self._city_address + ', ' + self._state_address + '\n' +
                vFunc.format_phone_num(self._phone_num) + '\n' +
                'Salaried Employee: $' + str(self._salary) + '/year' + '\n' +
                'Start Date: ' + str(self.__start_date) + '\n')

if __name__ == '__main__':
    salEmp = SalariedEmployee('Elsea', 'Paul', '1234 Place', 'Town', 'UT', '1234567890', '01-01-2001', 40000)
    print(salEmp.display())
    salEmp.give_raise(45000)
    print(salEmp.display())
    del(salEmp)