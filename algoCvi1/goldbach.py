import math


def sito(n):
    returningList = (n) * [False]

    prvocisla = []
    je_prv = [False,False,True,True] + int(((n-0.5)//2)-1)*[True]
    for p in range(2,int((n-0.5)//2)+3):
        if je_prv[p]:
            prvocisla.append(p if p<=3 else p+(p-3))
            returningList[p if p<=3 else p+(p-3)] = True
            if p == 2:
                continue
            for i in range(p,int((n-0.5)//2)+3,1+(p-2)*2):
                je_prv[i] = False
    return prvocisla, returningList



primesList = []
allNumbersPrime = []



def goldbachCount(number):


    if number in [0,1,2,3]:

        return 0

    elif number in [4,5]:

        return 1

    correctSums = set()

    if number % 2 == 1 : #pokud je cislo liche, goldbach conjecture muze platit jen pro dvojici 2 a (cislo-2)

        b = number - 2

        if allNumbersPrime[b]:

            return 1

        else:

            return 0


    else: # cislo je sude

        for i in range(len(primesList)):

            firstPrime = primesList[i]
            secondPrime = number - firstPrime

            if secondPrime < 2:
                continue

            if allNumbersPrime[secondPrime]:
                correctSums.add((min(firstPrime,secondPrime),max(firstPrime,secondPrime)))

        return len(correctSums)

def inputHandler(str):

    global primesList
    global allNumbersPrime

    strArr = str.split()

    strArr = [int(x) for x in strArr]

    primesList,allNumbersPrime = sito(max(strArr))

    final = ""

    for num in strArr:

        final += f"{goldbachCount(num)} "


    return final[:-1]


print(inputHandler(input()))




