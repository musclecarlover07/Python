class SumOverLoad():
    def __add__(self, other1):
        if isinstance(self, set):
            return self | other1
        elif self == '6':
            return '%s plus %s' % (self, other1)

        self = self + other1
        return self


sum1 = 14
sum2 = 26
totalSum = sum1 + sum2
print('The sum of {0} and {1} is {2}'.format(sum1, sum2, totalSum))


firstList = [0, 2, 4, 6, 8]
secondList = [10, 12, 14, 16, 18]

concatenatedNewList = firstList + secondList
print('The new list is {} '.format(concatenatedNewList))


beginningStr = "Python Programming Language "
endStr = "is fun to play with "

concatenatedString = beginningStr + endStr

print('The concatenated string is {} '.format(concatenatedString))


result = SumOverLoad.__add__('6', '20')

print("Example of overloading the _add_ method: " + result)

print("There are no issues with running the program in PyCharm")
