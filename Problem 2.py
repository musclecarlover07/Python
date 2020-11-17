# =====================================================================
#    Course: CS219 -- Problem 2 -- Garage List
#    Filename: Problem 2_<Micheal Smith>_Problem 2.py
#    Author: <Micheal Smith>
#    Purpose: 	Program tht creates a list of cars in a garage
#               and uses pop() to determine how long it will
#               take to retrieve the car.
# =====================================================================


garage_list = []


def main():
    while True:
        print("Select an option:")
        print(" (A)dd a car to the garage")
        print(" (R)etrieve a car")
        print(" (E)stimate time to retrieve car")
        print(" (Q)uit Program")

        user_input = input("> ")

        if user_input == "Q":
            break
        elif user_input == "A":
            add_car()
        elif user_input == "R":
            retrieve_car()
        elif user_input == "E":
            estimate_retrieve()
        else:
            print("Invalid Selection. Try again\n")


def add_car():
    # Add Data
    print("\nADD VEHICLE")
    print("How many vehicles would you like to add to the car?")
    num_cars = int(input("> "))

    while True:
        if num_cars >= 1:
            i = 1
            while i <= num_cars:
                # car_num = i - 1
                # garage_list[car_num].append(input("Car:"))
                garage_list.append(input("Car:"))
                i += 1
            i = 0
            while i < num_cars:
                i += 1

            print("Added", i, "vehicles(s) to the garage.\n")

            break
        elif num_cars < 1:
            print("Must input at least 1 record")
        else:
            print("Invalid value. Please Try again")


def retrieve_car():
    print("\nRETRIEVE CAR")

    for i in range(len(garage_list)):
        print(i + 1, garage_list[i])

    print("Which car would you like to remove:")
    remove_car = input("> ")

    garage_list.remove(remove_car)
    print("Car", remove_car, "was removed and no longer in the garage.")


def estimate_retrieve():
    print("\nESTIMATE")
    print("Which vehicle would you like to get an estimate for retrieval:")

    print("Garage: ", garage_list)

    temp_garage_list = garage_list.copy()

    car = input("> ")

    count = 0

    while temp_garage_list.pop() != car:
        count += 1

    estimate = (count + 1) * 5

    print("It will take", estimate, "minutes to retrieve your car")


main()
