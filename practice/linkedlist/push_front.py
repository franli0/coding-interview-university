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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def push_front_without_tail_pointer(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

def main():
    linkedlist = LinkedList()
    linkedlist.push_front_with_tail_pointer(1)
    linkedlist.push_front_with_tail_pointer(2)
    linkedlist.push_front_with_tail_pointer(3)
    print("Linked list with tail pointer:")
    for node in linkedlist:
        print(node.data)
    
    linkedlist = LinkedList()
    linkedlist.push_front_without_tail_pointer(1)
    linkedlist.push_front_without_tail_pointer(2)
    linkedlist.push_front_without_tail_pointer(3)
    print("Linked list without tail pointer:")
    for node in linkedlist:
        print(node.data)

if __name__ == "__main__":
    main()
