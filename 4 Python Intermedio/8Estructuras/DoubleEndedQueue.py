class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class DeQue:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def push_left(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def push_right(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def pop_left(self):
        if self.head:
            self.head = self.head.next
        return

    def pop_right(self):
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        return

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next



#Use of Double Ended Queue Structures
deque = DeQue()
deque.push_left("C")
deque.push_left("B")
deque.push_left("A")

deque.push_right("D")
deque.push_right("E")
deque.push_right("F")

print("Content of DEQue:")
deque.print_structure()

deque.pop_left()
deque.pop_right()

print("Final Content of DEQue:")
deque.print_structure()