class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front_with_tail_pointer(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def push_front_without_tail_pointer(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def pop_front_with_tail_pointer(self):
        if self.head is None:
            raise IndexError("Linked list is empty")
        value = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        return value
    
    def pop_front_without_tail_pointer(self):
        if self.head is None:
            raise IndexError("Linked list is empty")
        value = self.head.data
        self.head = self.head.next

        return value
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next 

def main():
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    linkedlist.head.next = Node(2)
    linkedlist.head.next.next = Node(3)
    linkedlist.head.next.next.next = Node(4)
    linkedlist.head.next.next.next.next = Node(5)

    print("Value poped with tail pointer:", linkedlist.pop_front_with_tail_pointer())
    print("Value poped without tail pointer:", linkedlist.pop_front_without_tail_pointer())

    for node in linkedlist:
        print(node.data)

if __name__ == "__main__":
    main()
