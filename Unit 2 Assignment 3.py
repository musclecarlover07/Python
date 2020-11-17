def main():
    employeesList = list()
    employeesList.append(HourlyBasePay("Mike", 1))
    employeesList.append(YearlyBasePay("Sarah", 2))

    for i in employeesList:
        i.calculateSalary()
        print(i.employeeName, "has salary of", i.salary,"each year.")

        print("There are no issues with running the program in PyCharm")


class Employee:
    # Constructor
    def __init__(self, employeeName, employeeID):
        self.employeeName = employeeName
        self.employeeID = employeeID
        self.salary = None

    # Memeber Function
    def calculateSalary(self):
        raise NotImplementedError("Need to use the abstract method.")


class HourlyBasePay(Employee):
    # Constructor
    def __init__(self, employeeName, employeeID):
        Employee.__init__(self, employeeName, employeeID)
        self.hoursWorked = None
        self.hourlyRate = None

    # Memeber Function
    def calculateSalary(self):
        self.hoursWorked = input("\nHow many hours does " + self.employeeName + " work each week?")
        self.hourlyRate = input("Hourly Rate:")
        self.salary = int(self.hoursWorked) * float(self.hourlyRate) * 52


class YearlyBasePay(Employee):
        # Constructor
        def __init__(self, employeeName, employeeID):
            Employee.__init__(self, employeeName, employeeID)
            self.yearsWorked = None
            self.basePay = None

        # Member Function
        def calculateSalary(self):
            self.yearsWorked = input("\nHow many years has " + self.employeeName + " worked for the company?")
            self.basePay = input("Base Pay:")
            self.salary = int(self.basePay) + (int(self.basePay)) * .10 * float(self.yearsWorked)


main()
