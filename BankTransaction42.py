class BankTransactions:
    # Constructors
    def __init__(self, initAmount = 0.0, initCode = 'D', initNote = 'No Note'):
        self.__Amount = 0.0
        self.setAmount(initAmount)

        self.__Code = 'D'
        self.setCode(initCode)

        self.__Note = 'No Note'
        self.setNote(initNote)


    # Setters
    def setAmount(self, newAmount):
        if newAmount >= 0.0:
            self.__Amount = newAmount
        else:
            self.__Amount = self.__Amount


    def setCode(self, newCode):
        if newCode == 'W' or newCode == 'D':
            self.__Code = newCode
        else:
            self.__Code = self.__Code


    def setNote(self, newNote):
        if len(newNote) > 0:
            self.__Note = newNote
        else:
            self.__Note = self.__Note


    # Getters
    def getAmount(self):
        return self.__Amount


    def getCode(self):
        return self.__Code


    def getNote(self):
        return self.__Note


    # Member Functions
    def enterTransAction(self):
        self.setAmount(float(input('Amount $: ')))
        self.setNote(input('Code W/D: '))
        self.setNote(input('Purpose: '))
