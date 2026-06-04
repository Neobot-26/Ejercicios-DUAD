class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def insert_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def delete(self,data):
        if self.head is None:
            self.head = None
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current=current.next

    def print_all(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

#Use of Double Ended Queue Structures
linkedlist = LinkedList()
linkedlist.insert_front(10)
linkedlist.insert_front(20)

linkedlist.insert_back(30)

print("Content of List:")
linkedlist.print_all()

linkedlist.delete(10)

print("Final Content of List:")
linkedlist.print_all()