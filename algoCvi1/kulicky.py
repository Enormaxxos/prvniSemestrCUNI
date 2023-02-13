import random

def applyLogic(b,c):
    arr = []

    for i in range(b):
        arr.append("b")
        
    for i in range(c):
        arr.append("c")

    while len(arr) > 1:
        ballOne = arr.pop(random.randrange(len(arr)))
        ballTwo = arr.pop(random.randrange(len(arr)))

        if ballOne == "b" and ballTwo == "b":
            arr.append(ballOne)
        elif (ballOne == "c" and ballTwo == "b"):
            arr.append(ballOne)
        elif (ballOne == "b" and ballTwo == "c"):
            arr.append(ballTwo)
        elif ballOne == "c" and ballTwo =="c":
            arr.append("b")


    print(f"b: {b}, c: {c},arr[0]: {arr[0]}")


for i in range(1,20):
    for j in range(1,20):
        applyLogic(i,j)
