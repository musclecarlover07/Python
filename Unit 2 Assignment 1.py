def main():
    customerListing = list()

    for i in range(0, 3):
        print("\nCustomer #", i+1)
        newCust = Customer()
        newCust.setCustName(input("Name:"))
        newCust.setCustAddress(input("Address:"))

        while not newCust.setCustPhone(input("Phone:")):
            print("Re-enter Phone")

        while not newCust.setCustBalace(input("Balance:")):
            print("Re-enter Balance")

        customerListing.append(newCust)

    print("\nCustomer Listing")
    for i in customerListing:
        print("  ", i.custName)

    selectCust = input("\nSelect a customer:")

    for i in range(0, 3):
        if customerListing[i].custName == selectCust:
            customerListing[i].customerInformation()

    print("There are no issues with running the program in PyCharm")


class Customer:
    # Constructor
    def __init__(self):
        self.custName = None
        self.custAddress = None
        self.custPhone = None
        self.custBalance = None

    # Setters
    def setCustName(self, name):
        self.custName = name

    def setCustAddress(self, address):
        self.custAddress = address

    def setCustPhone(self, phone):
        if len(phone) == 12:
            self.custPhone = phone
            return True
        else:
            print("Phone must be ###-###-####")
            return False

    def setCustBalace(self, balance):
        if int(balance) > 0:
            self.custBalance = balance
            return True
        else:
            print("Cannot have a negative balance")
            return False

    # Member Function
    def customerInformation(self):
        print(self.custName,
              "lives at", self.custAddress,
              "and can be called at", self.custPhone,
              "and owes $", self.custBalance)


main()
