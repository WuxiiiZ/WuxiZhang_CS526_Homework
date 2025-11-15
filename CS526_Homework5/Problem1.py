class Node:
    def __init__(self,value):
        self.value = value
        self.left = None        # left child
        self.right = None       # right child

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):       # add
        if self.root is None:
            self.root = Node(value)
        else:
            cur = self.root
            while cur:
                if value < cur.value:
                    if cur.left is None:
                        cur.left = Node(value)
                        return
                    cur = cur.left
                else:       # if value = cur.value, we put the node to the right child
                    if cur.right is None:
                        cur.right = Node(value)
                        return
                    cur = cur.right

    def find(self,value):
        cur = self.root
        while cur:
            if value < cur.value:
                    cur = cur.left
            elif value > cur.value:
                cur = cur.right
            elif value == cur.value:
                return cur
            
        return None
                    
    def delete(self,value):
        def delete_recursion(node,data):
            if not node:
                return None
            if data < node.value:
                node.left = delete_recursion(node.left, data)
                return node
            elif data > node.value:
                node.right = delete_recursion(node.right, data)
                return node
            else:
                if not node.left:
                    right_child = node.right
                    node = None
                    return right_child
                elif not node.right:
                    left_child = node.left
                    node = None
                    return left_child
                else:
                    temp = node.left
                    while temp.right:
                        temp = temp.right
                    node.value = temp.value
                    # this node becomes the root of a modified subtree; recurse to update it. 
                    node.left = delete_recursion(node.left, node.value)
                    return node
        self.root = delete_recursion(self.root,value)

    def printTree(self):
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        height = get_height(self.root)
        if height == 0:
            return []

        width = 2 ** height - 1
        tree = [[""] * width for _ in range(height)]

        def recursion(node, row, column):
            if not node:
                return
            tree[row][column] = str(node.value)
            if row + 1 >= height:
                return
            diff = 2 ** (height - 2 - row)
            if node.left:
                recursion(node.left,row+1, column-diff)
            if node.right:
                recursion(node.right,row+1, column+diff)

        recursion(self.root, 0, (width - 1) // 2)
        for row in tree:
            print(row)
            

    
    
    
# python3 Problem1.py
if __name__ == "__main__":
    print("Test for tree 1")
    tree1 = BST()
    for v in [1,2]:
        tree1.add(v)
    print("The original tree is: ")
    tree1.printTree()

    tree1.add(10)
    print("Test add() with value 10: ")
    tree1.printTree()   
    
    print(f"Test find() with example input 5: {tree1.find(5).value if tree1.find(5) else 'Not in the tree'}")
    print(f"Test find() with example input 0: {tree1.find(0) if tree1.find(0) else 'Not in the tree'}")

    tree1.delete(10)
    print("Test delete() with value 10:")
    tree1.printTree()

    tree1.delete(0)
    print("Edge case 1 - delete node that not in the tree:")
    tree1.printTree()
    
    tree1.add(1.00000001)
    print(f"Edge case 2 - add node with very small number: {tree1.find(0.00000001).value if tree1.find(5) else 'Not in the tree'}")
    tree1.printTree()

    print(f"{'-'*50}")

    print("Test for tree 2")
    tree2 = BST()
    for v in [5,3,2,4,6,7,8]:
        tree2.add(v)
    print("The original tree is: ")
    tree2.printTree()

    tree2.delete(5)
    print("Test delete() with deleting the root:")
    tree2.printTree()


    




        

                
                    


        
            
