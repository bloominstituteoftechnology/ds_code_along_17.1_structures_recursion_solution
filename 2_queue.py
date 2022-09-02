from collections import deque

class queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.popleft()

# Test cases:
myQueue = queue()
myQueue.enqueue(3)
myQueue.enqueue(6)
myQueue.enqueue(9)
print(myQueue.dequeue()) # 3
print(myQueue.dequeue()) # 6
print(myQueue.dequeue()) # 9
