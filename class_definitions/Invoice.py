"""
Program: Invoice.py
Author: Paul Elsea
Last Modified: 07/3/2020

Defining the Invoice class.
"""
from Validation_Utilities import Validation_Functions as vFunc

class Invoice:
    '''Invoice class constructor'''
    #Constructor
    def __init__(self, ivnum, idnum, lname, fname, addStr, addCity, addState, phone, items_price={}):
        self._inv_id = vFunc.valid_id_check(ivnum) #invoice ID, required: 10 digit number
        self._cust_id = vFunc.valid_id_check(idnum) #customer ID, required: 10 digit number
        self._last_name = vFunc.valid_alpha_check(lname) #last name, required: string
        self._first_name = vFunc.valid_alpha_check(fname) #first name, required: string
        self._street_address = vFunc.valid_alpha_num_check(addStr) #street address, required: string
        self._city_address = vFunc.valid_alpha_check(addCity) #city, required: string
        self._state_address = vFunc.state_abbrv_or_full(addState) #state, required: string
        self._phone_num = vFunc.valid_phone_check(phone) #phone number, required: 10 digit number
        self._items_with_price = items_price #item and price, optional: string and int/float

    '''Functions to change individual characteristics of an invoice object'''
    def set_inv_id(self, ivnum):
        self._inv_id = vFunc.valid_id_check(ivnum)

    def set_cust_id(self, idnum):
        self._cust_id = vFunc.valid_id_check(idnum)

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


    '''Function to add items and their price to item_entry_dict'''
    def add_item(self, item_entry_dict):
        self._items_with_price.update(item_entry_dict)


    '''Function to create output string based off an employee class'''
    def create_invoice(self):
        tax_rate = .07
        tax = 0
        grand_total = 0

        for item, price in self._items_with_price.items():
            print(item, ' : ', price)
            tax += round(price*tax_rate,2)
            grand_total += round(price*(1+tax_rate),2)
        print('Tax - $' + str('%.2f' % tax) + '\n'
              'Total - $' + str('%.2f' % grand_total))

if __name__ == '__main__':
    inv = Invoice(9874563210, 1234567890, 'Threepwood', 'Guy', '1234 Place', 'Town', 'UT', '1234567890')
    inv.add_item({'Noodles': 1.99})
    inv.add_item({'Drinks': 2.99})
    inv.add_item({'Fortune Cookie': 3.99})
    inv.create_invoice()
