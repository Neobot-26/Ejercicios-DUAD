class Node:
    data: int
    left:"Node"
    right:"Node"

    def __init__(self, data, next=None):
        self.data = data
        self.left = next
        self.right = next

class QueueNode:
    data: Node
    next: "QueueNode"
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = QueueNode(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise Exception("La cola está vacía")
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    # Verify if this is empty
    def is_empty(self):
        return self.front is None

class BinaryTree:
    root: Node
    def __init__(self, root=None):
        self.root = root
        
    # insert new nodes
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
            return
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            current = queue.dequeue()
            print(current.data)
            if current.left is not None:
                queue.enqueue(current.left)
            if current.right is not None:
                queue.enqueue(current.right)

#Use of Binary Structures
tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)
print("Content of the Binary Tree:")

tree.print_tree()