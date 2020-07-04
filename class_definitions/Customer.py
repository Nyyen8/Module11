"""
Program: Customer.py
Author: Paul Elsea
Last Modified: 07/3/2020

Defining the Customer class.
"""
from Validation_Utilities import Validation_Functions as vFunc

class Customer:
    '''Customer class constructor'''
    #Constructor
    def __init__(self, idnum, lname, fname, addStr, addCity, addState, phone):
        self._cust_id = vFunc.valid_id_check(idnum) #customer ID, required: 10 digit number
        self._last_name = vFunc.valid_alpha_check(lname) #last name, required: string
        self._first_name = vFunc.valid_alpha_check(fname) #first name, required: string
        self._street_address = vFunc.valid_alpha_num_check(addStr) #street address, required: string
        self._city_address = vFunc.valid_alpha_check(addCity) #city, required: string
        self._state_address = vFunc.state_abbrv_or_full(addState) #state, required: string
        self._phone_num = vFunc.valid_phone_check(phone) #phone number, required: 10 digit number


    '''Functions to change individual characteristics of an customer object'''
    def set_cust_id(self, idnum):
        self._cust_id = vFunc.valid_id_check(idnum) #customer ID, required: 10 digit number

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
        return (str(self._cust_id) + '\n' +
                (self._first_name) + ' ' + str(self._last_name) + '\n' +
                self._street_address + '\n' +
                self._city_address + ', ' + self._state_address + '\n' +
                vFunc.format_phone_num(self._phone_num) + '\n')

if __name__ == '__main__':
    customer1 = Customer(1234567890, 'Threepwood', 'Guy', '1234 Place', 'Town', 'UT', '1234567890')
    print(customer1.display())

    '''The following customer will cause an exception to be thrown in valid_id_check(), part of the Validation_Utilities
    module. The exception occurs before display() can be called.'''
    customer2 = Customer('abcd', 'Threepwood', 'Guy', '1234 Place', 'Town', 'UT', '1234567890')
    print(customer2.display())