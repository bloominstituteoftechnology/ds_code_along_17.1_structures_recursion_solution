class listNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def search(head, value):
    if(head is None):
        return False
    elif(head.value == value):
        return True
    else:
        return search(head.next, value)


# Test cases:
head = listNode(3)
head.next = listNode(6)
head.next.next = listNode(9)
# The linked list is 3 -> 6 -> 9 (3 is the head of the list)

print(search(head, 3)) # True
print(search(head, 0)) # False
print(search(head, 9)) # True
