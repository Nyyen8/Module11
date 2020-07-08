"""
Program: Manager.py
Author: Paul Elsea
Last Modified: 07/8/2020

Defining the Manager class.
"""
from Validation_Utilities import Validation_Functions as vFunc
from class_definitions.SalariedEmployee import SalariedEmployee
from class_definitions.Person import Person
from class_definitions.HourlyEmployee import HourlyEmployee

class Manager(SalariedEmployee, Person):
    '''Manager class constructor'''
    #Constructor
    def __init__(self, lname, fname, addStr, addCity, addState, phone, startDate, salary, department, direct_report = []):
        '''Employee object, required:
            # last name, required: string
            # first name, required: string
            # street address, required: string
            # city, required: string
            # state, required: string
            # phone number, required: 10 digit number'''
        super().__init__(lname, fname, addStr, addCity, addState, phone, startDate, salary)
        self._department = vFunc.valid_name_check(department)  # manager's department, required: alphabetic string
        self._direct_report = direct_report # employee types which report to this manager, required: alphabetic list


    '''Function to change individual characteristics of an employee object'''
    def set_department(self, department):
        self._department = vFunc.valid_name_check(department)  # manager's department, required: alphabetic string

    def set_direct_report_list(self, direct_report):
        self._direct_report = direct_report # employees which report to this manager, required: list of employee objects

    '''Function to display list of employees under manager'''
    def list_underlings(self):
        for minion in self._direct_report:
            if isinstance(minion, HourlyEmployee):
                print(minion.display())
            elif isinstance(minion, SalariedEmployee):
                print(minion.display())

    '''Function to create output string based off an employee class'''
    def display(self):
        return (str(self._first_name) + ' ' + str(self._last_name) + '\n' +
                self._street_address + '\n' +
                self._city_address + ', ' + self._state_address + '\n' +
                vFunc.format_phone_num(self._phone_num) + '\n' +
                'Manager: $' + str(self._salary) + '/year' + '\n' +
                'Start Date: ' + str(self._start_date) + '\n')

if __name__ == '__main__':
    salEmpA = SalariedEmployee('Bubbington', 'Bubba', '1234 Street', 'Burg', 'CT', '1234567890', '01-01-2002', 40000)
    hourEmp = HourlyEmployee('Bob', 'Billy', '1234 Place', 'Town', 'MT', '0123456789', '01-01-2001', 10)
    salEmpB = SalariedEmployee('名', '中文', '1234 Blvd', 'City', 'VA', '1234567890', '01-01-2002', 50000)


    testMgr = Manager('Elsea', 'Paul', '1234 Place', 'Town', 'UT', '1234567890', '07-08-2020', 40000,
                             'Fishing', [salEmpA, hourEmp, salEmpB])
    print(testMgr.display()) # this uses the display function from the Manager class
    testMgr.list_underlings() # this uses the display function either the SalariedEmployee or HourlyEmployee class,
                              # depending on the class of the employee object at that moment
    testMgr.give_raise(2000)
    print(testMgr.display()) # this uses the display function from the Manager class
    del(testMgr)
    del(salEmpA)
    del(hourEmp)
    del(salEmpB)