class Queue:
    def __init__(self,max):
        self.queue = [None] * max
        self.max = max
        self.current = 0
        self.currentEnd = 0

    def enqueue(self,val):
        if self.queue[self.currentEnd % self.max] != None:
            raise Exception("Queue is full")

        self.queue[self.currentEnd % self.max] = val
        self.currentEnd = (self.currentEnd + 1) % self.max

    def dequeue(self):
        if self.queue[self.current] == None:
            raise Exception("Queue is empty")
        self.current = (self.current + 1) % self.max
        returning = self.queue[self.current - 1]
        self.queue[self.current - 1] = None
        return returning


#DONE