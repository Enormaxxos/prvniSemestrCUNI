class Stack:
    def __init__(self):
        self.stack = []

    def push(self,a):
        self.stack.append(a)
        return True

    def pop(self):
        return self.stack.pop()

a = Stack()

for i in range(5):
    a.push(i)

for i in range(5):
    print(a.pop())

