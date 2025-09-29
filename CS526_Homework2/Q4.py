class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = self.tail = newNode 
            
        else:
            self.tail.next = newNode 
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1 


def calcSum(head, tail, size):
    if (size < 3) or (size % 2 == 0):
        return "The linked list must have odd length and >= 3."
    if (size == 3):
        return head.value + head.next.value + tail.value
    return calcSum(head.next, tail.prev, size-2)
        

# test
dll = DoublyLinkedList()
for value in [2, 4, 8, 10, 15, 29, 41]:
    dll.append(value)
dll2 = DoublyLinkedList()
for value in [1, 3, 5 , 7]:
    dll2.append(value)
dll3 = DoublyLinkedList()
for value in [1, 2, 4, 8, 12, 20, 25]:
    dll3.append(value)

print(calcSum(dll.head, dll.tail, dll.size))
print(calcSum(dll2.head, dll2.tail, dll2.size))
print(calcSum(dll3.head, dll3.tail, dll3.size))