class Node:
    data: str
    next: "Node"
    prev: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.prev = next


class DoubleLinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        
    def delete(self,data):
        if self.head is None:
            return
        current = self.head
        while current is not None:

            if current.data == data:
                if current.prev is None:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                
                if current.next is None:
                    self.tail = current.prev
                    if self.tail is not None:
                        self.tail.next = None
                else:
                    current.next.prev = current.prev
                return
            current = current.next    

    def print_forward(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def print_backward(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev        

#Use of Double Linked List Structures
dll = DoubleLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")
dll.prepend("X")

print("Content of DoubleLikedList:")
print("Print List Forward:")
dll.print_forward()
print("Print List Backward:")
dll.print_backward()

dll.delete("B")

print("Final Content of DoubleLinkedList:")
print("Print List Forward:")
dll.print_forward()
print("Print List Backward:")
dll.print_backward()