from collections import deque

def eqFunc(x):
    if x == 0:
        return 1
    elif x == 1:
        return -1
    return 0


def findStepCount(mapList, startPos):
    looping = True
    moveCount = 0

    stacks = [deque(), deque()]

    stacks[0].append(startPos)

    for placeholder in range(20):
        currStack = moveCount % 2

        # print("starting on new",stacks[currStack])

        while len(stacks[currStack]) > 0:
            # print("len=",len(stacks[currStack]))
            point = stacks[currStack].pop()
            canContinue = [True, True, True, True]  # UP,DOWN,LEFT,RIGHT
            dist = 0
            # print("point=",point)

            while any(canContinue):
                # print("----")
                # print(canContinue)
                # print(startPos)
                dist += 1
                for i in range(4):
                    if canContinue[i]:
                        try:
                            firstAdd = (point[0] + eqFunc(i) * dist)
                            secondAdd = point[1] + eqFunc(i-2) * dist
                            newCoords = (firstAdd if (firstAdd >= 0 and firstAdd < 8) else None, secondAdd if (
                                secondAdd >= 0 and secondAdd < 8) else None)
                            # print(f"new coords = {newCoords}")
                            pointChar = mapList[newCoords[0]][newCoords[1]]
                        except:
                            canContinue[i] = False
                            continue

                        if pointChar == "." or pointChar == "v":
                            stacks[(currStack + 1) %
                                   2].append((newCoords[0], newCoords[1]))
                            # print(f"adding {newCoords[0], newCoords[1]}")
                        elif pointChar == "x":
                            canContinue[i] = False
                        elif pointChar == "c":
                            return moveCount + 1

        moveCount += 1
        stacks[currStack].clear()

    return -1


def inputHandler():
    mapList = []

    startPos = None

    for i in range(8):
        mapRow = [*input()]
        mapList.append(mapRow)
        try:
            startPos = (i, mapRow.index("v"))
        except ValueError:
            continue

    final = findStepCount(mapList, startPos)
    return final


print(inputHandler())
