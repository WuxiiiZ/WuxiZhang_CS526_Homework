'''
Write a function that reverses a stack implemented as an array
'''

def reverseArray(arr, stack = None):
    if stack is None:
        stack = []
    temp = arr.copy()
    #base case: len(arr) = 0, or no element in arr
    if not temp:
        return stack
    element = temp.pop()
    stack.append(element)
    return reverseArray(temp, stack)

print("*This is test results of array:")
array1 = [1,2,4,5,3]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array3 = [1, 2, 4, 8, 16, 32, 64] 
array4 = [1, 0 , -1, 0, 1]
print(reverseArray(array1))
print(reverseArray(array2))
print(reverseArray(array3))
print(reverseArray(array4))


'''
Write a function that reverses a stack implemented as a Linked-list
'''
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def append(self, value):
        current = self
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def printLinkedList(self):
        head = self
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")

# Find the head of the new reversed linked list
def reverseLinkedList(head):
    if head is None or head.next is None:
        return head

    current = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return current

print("*This is test results of linked-list:")
node1 = Node(1)
for value in (2, 3, 4, 5, 6, 7, 8, 9, 10):
    node1.append(value) 
head1 = reverseLinkedList(node1)
head1.printLinkedList()

node2 = Node(1)
for value in (2, 4, 8, 16, 32, 64):
    node2.append(value) 
head2 = reverseLinkedList(node2)
head2.printLinkedList()

node3 = Node(1)
for value in (0 , -1, 0, 1):
    node3.append(value) 
head3 = reverseLinkedList(node3)
head3.printLinkedList()

'''
Write a function that reverses a stack implemented as a doubly linked-list
'''
class DNode:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

    def printDLL(self):
        head = self
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        newNode = DNode(value)
        if self.head is None:
            self.head = self.tail = newNode  
        else:
            self.tail.next = newNode 
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1 

def reverseDLL(head):
    if head is None or head.next is None:
        head.prev = None
        return head
    current = reverseDLL(head.next)
    head.next.next = head
    head.prev = head.next
    head.next = None
    return current

print("*This is test results of doubly linked-list:")

dll = DoublyLinkedList()
for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    dll.append(value)
head = reverseDLL(dll.head)
head.printDLL()

dll2 = DoublyLinkedList()
for value in [1, 2, 4, 8, 16, 32, 64]:
    dll2.append(value)
head2 = reverseDLL(dll2.head)
head2.printDLL()

dll3 = DoublyLinkedList()
for value in [1, 0 , -1, 0, 1]:
    dll3.append(value)
head3 = reverseDLL(dll3.head)
head3.printDLL()




