from collections import deque

class stack:
    def __init__(self):
        self.data = deque()

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()


# Test cases:
myStack = stack()
myStack.push(3)
myStack.push(6)
myStack.push(9)
print(myStack.pop()) # 9
print(myStack.pop()) # 6
print(myStack.pop()) # 3