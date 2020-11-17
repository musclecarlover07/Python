class Vehicle:
    # Constructor
    def __init__(self):
        self.vehicleColor = None
        self.vehiclePrice = None
        self.vehicleHP = None
        self.vehicleEngine = None

    #Setter
    def setUpVehicle(self):
        print("To add a vehicle to the inventory you will need to answer some questions.")
        self.vehicleColor = input("Vehicle Color: ")
        self.vehiclePrice = input("Vehicle Price: ")
        self.vehicleHP = input("Vehicle HP: ")
        self.vehicleEngine = input("Vehicle Engine: ")


class Car(Vehicle):
    # Constructor
    def __init__(self):
        Vehicle.__init__(self)
        self.doorCount = None
        self.bodyStyle = None

    # Setter
    def setUpCar(self):
        self.doorCount = input("Number of Doors: ")
        self.bodyStyle = input("Body Style: ")


class Truck(Vehicle):
    # Consturctor
    def __init__(self):
        Vehicle.__init__(self)
        self.wheelCount = None
        self.flatbed = None

    # Setter
    def setUpTruck(self):
        self.wheelCount = input("Number of Wheels: ")
        self.flatbed = input("Flatbed Y/N: ")


class Boat(Vehicle):
    # Constructor
    def __init__(self):
        Vehicle.__init__(self)
        self.boatTop = None
        self.boatLength = None

    # Setter
    def setUpBoat(self):
        self.boatTop = input("Boat Top Y/N: ")
        self.boatLength = input("Boat Length: ")


def main():
    # Needed Variales
    vehicle1 = Car()
    vehicle2 = Truck()
    vehicle3 = Boat()

    # Car Test
    vehicle1.setUpVehicle()
    vehicle1.setUpCar()

    # Truck Test
    vehicle2.setUpVehicle()
    vehicle2.setUpTruck()

    # Boat Test
    vehicle3.setUpVehicle()
    vehicle3.setUpBoat()

    print("There are no issues with running the program in PyCharm")


main()
