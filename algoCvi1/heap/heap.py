def heapSwitch(lst, lstLen, i):
    biggest = i
    leftChild = 2 * (i+1) - 1
    rightChild = 2 * (i+1)

    if leftChild < lstLen and lst[leftChild] > lst[biggest]:
        biggest = leftChild

    if rightChild < lstLen and lst[rightChild] > lst[biggest]:
        biggest = rightChild

    if biggest != i:
        temp = lst[i]
        lst[i] = lst[biggest]
        lst[biggest] = temp

        heapSwitch(lst, lstLen, biggest)


def heapSort(lst):
    final = ""

    n = len(lst)

    for i in range(n//2, -1, -1):
        heapSwitch(lst, n, i)

    for unit in lst:
        final += str(unit) + " "
    final = final[:-1]
    final += "\n"

    for i in range(n-1, 0, -1):
        temp = lst[i]
        lst[i] = lst[0]
        lst[0] = temp

        heapSwitch(lst, i, 0)
        for unit in lst:
            final += str(unit) + " "
        final = final[:-1]
        final += "\n"

    print(final[:-1])

def inputHandler():
    lstLen = int(input())
    lst = []

    for i in range(lstLen):
        lst.append(int(input()))

    heapSort(lst)

inputHandler()