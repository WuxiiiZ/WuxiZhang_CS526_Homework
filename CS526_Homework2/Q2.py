# Inplement node and function
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def doIt(node):
    if node is None:
        return
    doIt(node.next)
    print(node.value)

# Create a linked list with 12,3,5,2
head = Node(12)
head.next = Node(3)
head.next.next = Node(5)
head.next.next.next = Node(2)

# The doIt function will print the node value in the order 2 5 3 12
doIt(head)
