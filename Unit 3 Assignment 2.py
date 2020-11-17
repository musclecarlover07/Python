def main():
    dvdList = []

    dvd1 = DVD('Fifa 19', 'Game', 20)
    dvd2 = DVD('Die Hard', 'Compiler', 19.99)
    dvd3 = DVD('Lethal Weapon', 'Spreadsheet', 99.99)

    dvdList.append(dvd1)
    dvdList.append(dvd2)
    dvdList.append(dvd3)

    DVD.displayDvdInformation(dvdList)
    DVD.displayTotalAndAverage(dvdList)

    DVD.changeDvd(dvd1)
    DVD.changeDvd(dvd2)
    DVD.changeDvd(dvd3)

    newDvdList = []

    newDvdList.append(dvd1)
    newDvdList.append(dvd2)
    newDvdList.append(dvd3)

    DVD.displayDvdInformation(newDvdList)
    DVD.displayTotalAndAverage(newDvdList)

    print("There are no issues with running the program in PyCharm")


class DVD:
    # Constructor
    def __init__(self, initDvdTitle, initDvdType, initDvdCost):
        self.dvdTitle = initDvdTitle
        self.dvdType = initDvdType
        self.dvdCost = initDvdCost

    # Setters
    def setDvdTitle(self, newDvdTitle):
        self.dvdTitle = newDvdTitle


    def setDvdType(self, newDvdType):
        dvdTypeList = ['Compiler', 'Dbase', 'Game', 'Presentation', 'Spreadsheet', 'Word']

        while True:
            DVD.listValidDvdType(self)
            self.dvdType = input('DVD Type: ')

            if self.dvdType not in dvdTypeList:
                print('Invalid Choice. Try Again: ')
                continue
            else:
                self.dvdType = newDvdType
            break


    def setDvdCost(self, newDvdCost):
        self.dvdCost = newDvdCost

    # Getters
    def getDvdTitle(self):
        return self.dvdTitle


    def getDvdType(self):
        return self.dvdType


    def getDvdCost(self):
        return self.dvdCost


    # Member Functions
    def displayTotalAndAverage(listOfDvd):
        total = 0

        for i in listOfDvd:
            total += i.dvdCost

        # print('\nTotal: $', total)
        print('Total ${:0,.2f}'.format(total))
        print('Average ${:0,.2f}'.format(total / len(listOfDvd)))

        # print('Average Cost: $', total / len(listOfDvd))


    def displayDvdInformation(listOfDvd):
        print('Info')
        print('Name', ' ' * (20 - len('Name')),
              'Type', ' ' * (15 - len('Type')),
              'Cost', ' ' * (6 - len('Cost'))
                )

        for i in listOfDvd:
            print(i.dvdTitle, ' ' * (20 - len(i.dvdTitle)),
                  i.dvdType, ' ' * (15 - len(i.dvdType)),
                  i.dvdCost, ' ' * (6 - len(str(i.dvdCost)))
            )


    def listValidDvdType(self):
        print(' List of Valid DVD Types: ')
        print('  Compiler')
        print('  Dbase')
        print('  Game')
        print('  Presentation')
        print('  Spreadsheet')
        print('  Word')


    def changeDvd(aDvd):
        # Change Title
        print('\nTitle:', aDvd.dvdTitle)
        dvdTitleChange = input('Do you want to change the title? y/n ')

        if dvdTitleChange in ['y', 'Y']:
            titleChange = input('Title Change: ')
            aDvd.dvdTitle = titleChange
            print('DVD title changed to', aDvd.dvdTitle, 'successfully.')
        else:
            pass

        # Change Type
        print('\nType:', aDvd.dvdType)
        dvdTypeChange = input('Do you want to change the type? y/n ')
        
        if dvdTypeChange in ['y', 'Y']:
            dvdTypeList = ['Compiler', 'Dbase', 'Game', 'Presentation', 'Spreadsheet', 'Word']

            DVD.listValidDvdType(DVD)

            while True:
                typeChange = input('New DVD Type:')

                if typeChange.title() not in dvdTypeList:
                    print('Invalid Choice. Try Again.')
                    continue
                else:
                    aDvd.dvdType = typeChange
                    print('DVD type changed to ', aDvd.dvdType, ' successfully')
                    break
            else:
                pass

        # Change Cost
        print('\nCost:', aDvd.dvdCost)
        dvdCostChange = input('Do you want to change the cost? y/n ')

        if dvdCostChange in ['y', 'Y']:
            costChange = float(input('Cost Change: '))
            aDvd.dvdCost = costChange
        else:
            pass


main()
