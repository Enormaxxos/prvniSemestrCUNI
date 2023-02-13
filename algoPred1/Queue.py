class Queue:
    def __init__(self):
        self.queue = []
        zacatek = 0
    
    def enqueue(self,a):
        self.queue.append(a)
        return True
    def dequeue(self):
        zacatek += 1
        return self.queue[zacatek-1]

a = Queue()

for i in range(5):
    a.enqueue(i)

a
