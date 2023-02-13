a = []

missing = 14

for i in range(20):
    if i == missing:
        continue
    a.append(i)



def find(arr):

    startIn = 0
    endIn = len(arr)

    while endIn-startIn > 1:
        midIn = (endIn+startIn)//2

        if arr[midIn] == midIn:
            startIn = midIn
            endIn = endIn
        else:
            startIn = startIn
            endIn = midIn

    return (arr[startIn] + arr[endIn])//2


print(find(a.copy()))


