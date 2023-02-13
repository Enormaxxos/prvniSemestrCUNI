from collections import deque

def findComponents(hrany):
    remainingPoints = list(range(1,len(hrany)))
    components = []

    while len(remainingPoints) > 0:
        newComponent = []
        newStack = deque()
        newStack.append(remainingPoints[0])

        while len(newStack) > 0:
            # print('newStack',newStack)
            newPoint = newStack.pop()
            newComponent.append(newPoint)
            # print('remaining points =', remainingPoints)
            # print('newPoint =', newPoint)
            remainingPoints.remove(newPoint)

            # print('hrany',hrany)
            # print('newPoint',newPoint)
            for soused in hrany[newPoint]:
                if soused not in newComponent and soused not in newStack:
                    newStack.append(soused)
        components.append(newComponent)

    return components

def inputHandler():
    pocetVrcholu = int(input())
    pocetHran = int(input())

    hrany = [None]
    for i in range(pocetVrcholu):
        hrany.append([])

    for i in range(pocetHran):
        vrchol1, vrchol2 = [int(i) for i in input().split(" ")]
        hrany[vrchol1].append(vrchol2) 
        hrany[vrchol2].append(vrchol1) 

    # print(hrany)

    komponenty = findComponents(hrany)
    final = ""

    for komponenta in komponenty:
        for unit in komponenta:
            final += str(unit) + " "
        final = final[:-1] + "\n"

    return final[:-1]

print(inputHandler())