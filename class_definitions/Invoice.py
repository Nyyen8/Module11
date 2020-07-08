"""
Program: Invoice.py
Author: Paul Elsea
Last Modified: 07/7/2020

Defining the Invoice class.
"""
from Validation_Utilities import Validation_Functions as vFunc
from class_definitions import Customer

class Invoice:
    '''Invoice class constructor'''
    #Constructor
    def __init__(self, ivnum, cust, items_price={}):
        self._inv_id = vFunc.valid_id_check(ivnum) #invoice ID, required: 10 digit number
        '''customer object, required:
            #customer ID, required: 10 digit number
            #last name, required: string
            #first name, required: string
            #street address, required: string
            #city, required: string
            #state, required: string
            #phone number, required: 10 digit number'''
        self._customer = cust
        self._items_with_price = items_price #item and price, optional: string and int/float

    '''Functions to change individual characteristics of an invoice object'''
    def set_inv_id(self, ivnum):
        self._inv_id = vFunc.valid_id_check(ivnum)

    def set_cust(self, cust):
        self._customer = cust


    '''Function to add items and their price to item_entry_dict'''
    def add_item(self, item_entry_dict):
        self._items_with_price.update(item_entry_dict)


    '''Function to create output string based off invoice item_entry_dict contents'''
    def create_invoice(self):
        tax_rate = .07
        tax = 0
        grand_total = 0

        print(self._customer.display())

        for item, price in self._items_with_price.items():
            print(item.ljust(22, '.') + '$' + str(price))
            tax += round(price*tax_rate, 2)
            grand_total += round(price*(1+tax_rate),2)
        print('Tax'.ljust(22, '.') + '$' + str('%.2f' % tax) + '\n'
              'Total'.ljust(23, '.') + '$' + str('%.2f' % grand_total))

if __name__ == '__main__':
    new_customer = Customer.Customer(1234567890, 'Threepwood', 'Guy', '1234 Place', 'Town', 'UT', '1234567890')
    inv = Invoice(9874563210, new_customer)
    inv.add_item({'Noodles': 1.99})
    inv.add_item({'Drinks': 2.99})
    inv.add_item({'Fortune Cookie': 3.99})
    inv.create_invoice()
