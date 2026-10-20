class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_all(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def enqueue(self, new_node):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def dequeue(self):
        if self.head:
          self.head = self.head.next

    def bubble_sort(self):
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if current.data > current.next.data:
                    current.data, current.next.data = (
                        current.next.data,
                        current.data
                    )
                    swapped = True
                current = current.next



first_node = Node(4)
my_queue = Queue(first_node)

second_node = Node(2)
my_queue.enqueue(second_node)

third_node = Node(3)
my_queue.enqueue(third_node)

fourth_node = Node(1)
my_queue.enqueue(fourth_node)
print("Print Queue List Before Sorting:")
my_queue.print_all()

my_queue.bubble_sort()
print("Print Queue List After Sorting:")
my_queue.print_all()




