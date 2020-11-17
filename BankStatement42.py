from BankTransaction42 import BankTransactions

class BankStatement:
    # Constructor
    def __init__(self, initBalance = 0.0):
        self.__startBalance = initBalance
        self.__endBalance = initBalance
        self.__transactionLog = []
        self.__arrangedLog = []
        self.__runningBalanceLog = []
        self.__entryCount = 0
        self.__depositCount = 0
        self.__withdrawlCount = 0


    # Setter
    def setStartEndBalance(self, startEndBalance):
        self.__startBalance = self.__endBalance = startEndBalance


    # Getter
    def getStartBalance(self):
        return self.__startBalance


    def getEndBalance(self):
        return self.__endBalance


    def getEntryCount(self):
        return self.__entryCount


    def getDepositCount(self):
        return self.__depositCount


    def getWithdrawlCount(self):
        return self.__withdrawlCount


    # Member Functions
    def logTransaction(self, transaction):
        self.__transactionLog.append(transaction)
        self.__entryCount += 1

        if transaction.getCode() == 'D':
            self.__depositCount += 1

            if len(self.__runningBalanceLog) > 0:
                self.__endBalance = self.__runningBalanceLog[-1] + transaction.getAmount()
                self.__runningBalanceLog.append(self.__endBalance)

            else:
                self.__endBalance = self.getStartBalance() + transaction.getAmount()
                self.__runningBalanceLog.append(self.__endBalance)
        else:
            self.__withdrawlCount += 1

            if len(self.__runningBalanceLog) > 0:
                self.__endBalance = self.__runningBalanceLog[-1] - transaction.getAmount()
                self.__runningBalanceLog.append(self.__endBalance)
            else:
                self.__endBalance = self.getStartBalance() - transaction.getAmount()
                self.__runningBalanceLog.append(self.__endBalance)


    def displayBalances(self):
        print('Starting Balance: ${:0,.2f}'.format(self.__startBalance))

        for index, i in enumerate(self.__transactionLog):
            print('\nTransaction ' + str(index + 1 ) + ' was a ' + i.getCode() + ' amount: ${:0,.2f}'.format(i.getAmount()) + ' for ' + i.getNote())
            print('Running Balance: ${:0,.2f}'.format(self.__runningBalanceLog[index]))

        print('\nEnding Balance: ${:0,.2f}'.format(self.__endBalance))
        print('Transaction Count: ' + str(self.__entryCount))
        print('Deposit Count: ' + str(self.__depositCount))
        print('Withdrawl Count: ' + str(self.__withdrawlCount))


    def transactionArrangement(self):
        self.__arrangedLog.clear()

        for i in self.__transactionLog:
            if i.getCode() == 'D':
                self.__arrangedLog.append(i)

        for i in self.__transactionLog:
            if i.getCode() == 'W':
                self.__arrangedLog.append(i)


    def printArangedTransaction(self):
        print("\n'D'eposits and 'W'ithdrawls:")

        print(' Deposits')
        for index, i in enumerate(self.__arrangedLog):
            if i.getCode() == 'D':
                print('  Transaction was a', i.getCode(), 'amount ${:0,.2f}'.format(i.getAmount()), 'for ' + i.getNote())

        print(' Withdrawls')
        for index, i in enumerate(self.__arrangedLog):
            if i.getCode() == 'W':
                print('  Transaction was a', i.getCode(), 'amount ${:0,.2f}'.format(i.getAmount()), 'for ' + i.getNote())


    def printDepositTotal(self):
        depositTotal = 0.0

        for index, i in enumerate(self.__transactionLog):
            if i.getCode() == 'D':
                depositTotal = depositTotal + i.getAmount()

        print('Total Deposits: ${:0,.2f}'.format(depositTotal))


    def printWithdrawlTotal(self):
        withdrawlTotal = 0.0

        for index, i in enumerate(self.__transactionLog):
            if i.getCode() == 'W':
                withdrawlTotal = withdrawlTotal + i.getAmount()
        print('Total Withdrawls: ${:0,.2f}'.format(withdrawlTotal))


def main():
    mikesStatement = BankStatement()
    mikesStatement.setStartEndBalance(250.00)

    transaction1 = BankTransactions()
    transaction1.setAmount(99.22)
    transaction1.setCode('D')
    transaction1.setNote('Base Pay')

    transaction2 = BankTransactions()
    transaction2.setAmount(1000.50)
    transaction2.setCode('D')
    transaction2.setNote('Tax Refund')

    transaction3 = BankTransactions()
    transaction3.setAmount(46.85)
    transaction3.setCode('W')
    transaction3.setNote('Utilities')

    transaction4 = BankTransactions()
    transaction4.setAmount(6.50)
    transaction4.setCode('D')
    transaction4.setNote('ATM surcharge')

    transaction5 = BankTransactions(23.40, 'W', 'Eating Out')
    transaction6 = BankTransactions(650.53, 'W', 'Rent')
    transaction7 = BankTransactions(75.00, 'W', 'Gift')
    transaction8 = BankTransactions(123.26, 'W', 'Groceries')

    mikesStatement.logTransaction(transaction1)
    mikesStatement.logTransaction(transaction2)
    mikesStatement.logTransaction(transaction3)
    mikesStatement.logTransaction(transaction4)
    mikesStatement.logTransaction(transaction5)
    mikesStatement.logTransaction(transaction6)
    mikesStatement.logTransaction(transaction7)
    mikesStatement.logTransaction(transaction8)

    mikesStatement.displayBalances()
    mikesStatement.printDepositTotal()
    mikesStatement.printWithdrawlTotal()

    mikesStatement.transactionArrangement()
    mikesStatement.printArangedTransaction()

    print("There are no issues with running the program in PyCharm")


main()