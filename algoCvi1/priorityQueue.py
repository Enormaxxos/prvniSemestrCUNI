class PriorityQueue:
    def __init__(self):
        self.queueList = []

    def __str__(self):
        final = "["
        for obj in self.queueList:
            final += str((obj.name, obj.priority)) + ", "
        final = final[:-2]
        final += "]"
        return final

    def enqueue(self, new):
        self.queueList.append(new)
        currPos = len(self.queueList)-1

        looping = True

        while looping:
            looping = False

            parent = (currPos-1) // 2
            if parent >= 0 and self.queueList[parent].priority < new.priority:
                self.queueList[parent], self.queueList[currPos] = self.queueList[currPos], self.queueList[parent]

                currPos = parent
                looping = True

    def dequeue(self):
        if len(self.queueList) < 1:
            return None

        if len(self.queueList) == 1:
            return self.queueList.pop()

        returning = self.queueList[0]
        self.queueList[0] = self.queueList.pop()

        currPosIndex = 0
        looping = True
        while looping:
            looping = False

            childOneIndex = currPosIndex * 2 + 1
            childTwoIndex = childOneIndex + 1

            childOne = self.queueList[childOneIndex] if (
                childOneIndex < len(self.queueList)) else None
            childTwo = self.queueList[childTwoIndex] if (
                childTwoIndex < len(self.queueList)) else None

            if childOne == None == childTwo:
                continue

            elif childOne == None or childTwo == None:
                biggerChildIndex = childOneIndex if childOne else childTwo

            else:

                biggerChildIndex = childOneIndex if childOne is max(
                    [childOne, childTwo], key=lambda child: child.priority) else childTwoIndex

                if self.queueList[biggerChildIndex].priority > self.queueList[currPosIndex].priority:
                    looping = True
                    self.queueList[biggerChildIndex], self.queueList[currPosIndex] = self.queueList[currPosIndex], self.queueList[biggerChildIndex]
                    currPosIndex = biggerChildIndex

        return returning


class QueueUnit:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


queue = PriorityQueue()
final = ""

mainloop = True
while mainloop:
    instruction,*args = input().split()
    if instruction == "ENQUEUE":
        queue.enqueue(QueueUnit(args[0],int(args[1])))

    if instruction == "DEQUEUE":
        unit = queue.dequeue()
        print(unit.name,unit.priority)

    if instruction == "DONE":
        mainloop = False
