"""
Program: Address.py
Author: Paul Elsea
Last Modified: 07/8/2020

Defining the Address class.
"""
from Validation_Utilities import Validation_Functions as vFunc

class Address:
    '''Address class constructor'''
    #Constructor
    def __init__(self, addStr, addCity, addState):
        self._street_address = vFunc.valid_alpha_num_check(addStr)  # street address, required: string
        self._city_address = vFunc.valid_alpha_check(addCity)  # city, required: string
        self._state_address = vFunc.state_abbrv_or_full(addState)  # state, required: string

    '''Functions to change individual characteristics of an employee object'''
    def change_street_address(self, addStr):
        self._street_address = vFunc.valid_alpha_num_check(addStr) #street address, required: string

    def change_city_address(self, addCity):
        self._city_address = vFunc.valid_alpha_check(addCity) #city, required: string

    def change_state_address(self, addState):
        self._state_address = vFunc.state_abbrv_or_full(addState) #state, required: string

    '''Function to create output string based off an employee class'''
    def display(self):
        return (self._street_address + '\n' + self._city_address + ', ' + self._state_address + '\n')

if __name__ == '__main__':
    test_address = Address('1234 Place', 'Town', 'UT')
    print(test_address.display())