# Problem You are tasked with writing a new program for your company that keeps track of the customer’s information and his or her current bill.
# The company wants the name, address, phone number, and balance to be stored for each customer.
# This program will demonstrate the following:
# •	How to use a class to organize data
# •	How to use methods to access the data of a class
# •	How to create objects from a class


class CustomerInformation:
    def __init__(self):
        self.name = None
        self.address = None
        self.phone = None
        self.balance = None

    def setCustomerName(self, name):
        self.name = name

    def setCustomerAddress(self, address):
        self.address = address

    def setCustomerPhone(selfself, phone):
        if