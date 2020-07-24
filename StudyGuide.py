''' Study Guide '''

# Question 1
def divmod (aTuple):
    quotient = aTuple [0] // aTuple [1]
    remainder = aTuple [0] % aTuple [1]
    return (quotient, remainder)

myTuple = (3, 2)
question1 = divmod (myTuple)
print ("This should be 1,1:", question1)


# Question 2
def tupleInList (listOfTuples, aTuple):
    for num1, num2 in listOfTuples:
        if (num1 == aTuple[0]) and (num2 == aTuple [1]):
            return True
    return False

tupleList = [(1,1), (2,2), (3,3), (4,4), (5,5)]
isIn = tupleInList (tupleList, (3,3))
print ("This should be true:", isIn)
notIn = tupleInList (tupleList, (3,4))
print ("This should be false:", notIn)


# Question 3
import math
def highs (listOfDicitionaries):
    highList = []
    highestNum = -math.inf
    for dict in listOfDicitionaries:
        highList.append (dict ['high'])
        if (dict['high']) > highestNum:
            highestNum = dict['high']
    return (highList, highestNum)

# Question 4
for i in range (100):
    if (i+1) % 2 == 0:
        print (i + 1)













