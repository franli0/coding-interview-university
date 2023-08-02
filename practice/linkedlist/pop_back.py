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
    
    def pop_back_with_tail_pointer(self):
        if self.head is None:
            return None

        if self.head == self.tail:
            value = self.head.data
            self.head = None
            self.tail = None
            return value

        node = self.head
        while node.next.next is not None:
            node = node.next
        value = node.next.data
        node.next = None
        self.tail = node

        return value
    
    def pop_back_without_tail_pointer(self):
        if self.head is None:
            return None

        node = self.head
        while node.next.next is not None:
            node = node.next
        value = node.next.data
        node.next = None

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
    # linkedlist.push_front_with_tail_pointer(1)
    # linkedlist.push_front_with_tail_pointer(2)
    # linkedlist.push_front_with_tail_pointer(3)
    print("Value poped with tail pointer:", linkedlist.pop_back_with_tail_pointer())
    for node in linkedlist:
        print(node.data)

    linkedlist = LinkedList()
    linkedlist.head = Node(4)
    linkedlist.head.next = Node(5)
    linkedlist.head.next.next = Node(6)
    # linkedlist.push_front_without_tail_pointer(4)
    # linkedlist.push_front_without_tail_pointer(5)
    # linkedlist.push_front_without_tail_pointer(6)
    print("Value poped without tail pointer:", linkedlist.pop_back_without_tail_pointer())
    for node in linkedlist:
        print(node.data)

if __name__ == "__main__":
    main()