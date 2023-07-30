class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def pop_back_with_tail_pointer(self):
        if LinkedList is None:
            return None

        if self.tail is None:
            return None
        
        node = self.head
        while node.next is not self.tail:
            node = node.next
        value = self.tail.data
        self.tail = node
        self.tail.next = None

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

def main():
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    linkedlist.head.next = Node(2)
    linkedlist.head.next.next = Node(3)
    print(linkedlist.pop_back_with_tail_pointer())
    print(linkedlist.pop_back_without_tail_pointer())

if __name__ == "__main__":
    main()