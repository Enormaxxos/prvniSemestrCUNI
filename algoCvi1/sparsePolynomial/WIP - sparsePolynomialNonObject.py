from fractions import Fraction

def division(first,second):
    final = dict()

    firstSortedKeys = sorted(first,reverse=True)
    secondSortedKeys = sorted(second,reverse=True)

    # print(first)
    # print(second)
    startingKey = firstSortedKeys[0]

    for mainKey in range(startingKey,-1,-1):
        try:
            first[mainKey]
        except KeyError:
            continue
        finalPower = mainKey - secondSortedKeys[0]
        if finalPower < 0:
            continue

        # print(f"mainKey = {mainKey}, secondSortedKeys[0] = {secondSortedKeys}, finalPower = {finalPower}")

        numerator = Fraction(first[mainKey]).limit_denominator()
        denominator = Fraction(second[secondSortedKeys[0]]).limit_denominator()
        if denominator < 0:
            numerator *= -1
            denominator *= -1

        finalValue = Fraction(numerator/denominator).limit_denominator()
        final[finalPower] = finalValue

        for secondKey in secondSortedKeys:
            try:
                # print(second[secondKey])
                first[finalPower + secondKey] -= finalValue * second[secondKey]
                # print("substracting finalValue * second[secondKey] =",finalValue * second[secondKey])  
            except KeyError:
                first[finalPower + secondKey] = -finalValue * second[secondKey]
                # print("new finalValue * second[secondKey] =",finalValue * second[secondKey])  


    return first,final


def multiplication(first,second):
    final = dict()

    for powerOne,valueOne in first.items():
        for powerTwo, valueTwo in second.items():
            try:
                final[powerOne + powerTwo] += valueOne * valueTwo
            except KeyError:
                final[powerOne + powerTwo] = valueOne * valueTwo

    

    return final

def addition(first,second):
    final = dict()

    uniquePowers = set()
    for power in first.keys():
        uniquePowers.add(power)
    for power in second.keys():
        uniquePowers.add(power)

    for power in uniquePowers:
        a = 0
        b = 0

        try:
            a = first[power]
        except KeyError:
            a = 0
            
        try:
            b = second[power]
        except KeyError:
            b = 0

        final[power] = a + b

    return final



def inputHandler(string):
    strLines = string.split("\n")

    keyword = strLines[0]
    strLines = strLines[1:]

    sepIndex = strLines.index('-1 -1')

    firstPolyStrList = strLines[0:sepIndex]
    # print(firstPolyStrList, 'firstPolyStrList')
    
    secondPolyStrList = strLines[sepIndex+1:len(strLines)-1]
    # print(secondPolyStrList, 'secondPolyStrList')

    firstPolyDict = dict()
    secondPolyDict = dict()

    for firstPolyStrUnit in firstPolyStrList:
        firstPolyUnitList = firstPolyStrUnit.split(" ")
        firstPolyDict[int(firstPolyUnitList[0])] = int(firstPolyUnitList[1])

    for secondPolyStrUnit in secondPolyStrList:
        secondPolyUnitList = secondPolyStrUnit.split(" ")
        secondPolyDict[int(secondPolyUnitList[0])] = int(secondPolyUnitList[1])



    # print(keyword)
    # print(firstPolyDict)
    # print(secondPolyDict)

    if keyword == "add":
        final = ""
        a = addition(firstPolyDict,secondPolyDict)
        sortedKeys = sorted(a,reverse=True)

        for key in sortedKeys:
            if a[key] != 0:
                final += f"{key} {a[key]}\n"

        final += '-1 -1'

        return final

    elif keyword == "mul":
        final = ""
        a = multiplication(firstPolyDict,secondPolyDict)
        sortedKeys = sorted(a,reverse=True)

        for key in sortedKeys:
            if a[key] != 0:
                final += f"{key} {a[key]}\n"

        final += '-1 -1'

        return final
    elif keyword =="div":
        finalString = ""
        remainder, final = division(firstPolyDict,secondPolyDict)
        sortedFinalKeys = sorted(final,reverse=True)
        sortedRemainderKeys = sorted(remainder,reverse=True)

        for key in sortedFinalKeys:
            if final[key] != 0:
                finalString += f"{key} {final[key]}\n"

        finalString += '-1 -1\n'

        for key in sortedRemainderKeys:
            if remainder[key] != 0:
                finalString += f"{key} {remainder[key]}\n"

        finalString += '-1 -1'

        return finalString

    else:
        print("not recognised")

inputString = ""
inputBit = input()

while inputBit != "-1 -1":
    inputString += f"{inputBit}\n"
    inputBit = input()

inputString += f"{inputBit}\n"
inputBit = input()

while inputBit != "-1 -1":
    inputString += f"{inputBit}\n"
    inputBit = input()

inputString += f"{inputBit}"

print(inputHandler(inputString))


# 1b,c
# 2lez
# 3e
# 4 
# 5lez

