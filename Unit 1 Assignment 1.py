donor_list = list()


def main():
    while True:
        print("Select an option:")
        print(" (A)dd a new donor")
        print(" (E)dit a record")
        print(" (L)ook up a record")
        print(" (Q)uit Program")

        user_input = input("> ")

        if user_input == "Q":
            break
        elif user_input == "A":
            add_data()
        elif user_input == "E":
            edit_info()
        elif user_input == "L":
            look_up()
        else:
            print("Invalid Selection. Try again\n")

    print("There are no issues with running the program in PyCharm")


def add_data():
    # Add Data
    print("\nADD INFORMATION")
    print("How many records would you like to input")
    num_records = int(input("> "))

    while True:
        # Checks for a valid value. Must be an int greater than 0
        if num_records >= 1:

            # Check to see if the is any records
            list_len = len(donor_list)

            # Creates empty lists in donor_list = num_records
            i = 0
            while i < num_records:
                donor_list.append(list())
                i += 1

            j = 1
            # Checks to see if there is an empty list before the records are created
            if list_len == 0:
                while j <= num_records:
                    record_num = j - 1
                    print("\nRecord Number:", record_num + 1)
                    donor_list[record_num].append(input("Name:"))
                    donor_list[record_num].append(input("Address:"))
                    donor_list[record_num].append(input("Contact:"))
                    j += 1
            else:
                while j <= num_records:
                    record_num = list_len
                    print("\nRecord Number:", j)
                    donor_list[record_num].append(input("Name:"))
                    donor_list[record_num].append(input("Address:"))
                    donor_list[record_num].append(input("Contact:"))

                    j += 1
                    list_len += 1

            print("Created", i, "record(s)\n")
            break
        elif num_records < 1:
            print("Must input at least 1 record")
        else:
            print("Invalid value. Please Try again")


def edit_info():
    # Edit info
    print("EDIT INFORMATION")
    print("Enter the Record you wish to modify")
    look_up()
    record_num = int(input("Record: ")) - 1

    print("Select which element of the record you wish to modify")
    print("'0' = Name")
    print("'1' = Address")
    print("'2' = Contact")
    element_num = int(input("Element: "))

    while True:
        if element_num == 0:
            donor_list[record_num][element_num] = input("Name: ")
            break
        elif element_num == 1:
            donor_list[record_num][element_num] = input("Address: ")
            break
        elif element_num == 2:
            donor_list[record_num][element_num] = input("Contact: ")
            break
        else:
            print("Invalid Selection")


def look_up():
    print("\nINFO")
    print(
        "#", " " * (2 - len("#")),
        "Name", " " * (15 - len("Name")),
        "Address", " " * (20 - len("Address")),
        "Contact", " " * (10 - len("Contact"))
    )
    j = 1
    for i in donor_list:
        if j < 10:
            record = "0" + str(j)
        else:
            record = str(j)

        print(
            record, " " * (2 - len(i)),
            i[0], " " * (15 - len(i[0])),
            i[1], " " * (20 - len(i[1])),
            i[2], " " * (10 - len(i[2])),
        )

        j += 1

    print("\n")


main()
