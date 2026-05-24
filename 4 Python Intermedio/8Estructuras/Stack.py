class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def pop(self):
        if self.head:
            self.head = self.head.next

#Use of Stack Structures
stack = Stack()
stack.push("10")
stack.push("20")
stack.push("30")
stack.push("40")

print("Final Content of Stack")
stack.print_structure()

print("First POP")

stack.pop()
stack.print_structure()

print("Second POP")

stack.pop()
stack.print_structure()

print("Third POP")

stack.pop()
stack.print_structure()

print("Forth POP")

stack.pop()
stack.print_structure()


print("POP")

stack.pop()
stack.print_structure()