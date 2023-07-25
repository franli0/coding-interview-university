class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def size_with_tail_pointer(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count
    
    def size_without_tail_pointer(self):
        count = 0
        node = self.head
        while node.next is not None:
            count += 1
            node = node.next
        return count

def main():
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    linkedlist.head.next = Node(2)
    linkedlist.head.next.next = Node(3)
    print("Size with tail pointer:", linkedlist.size_with_tail_pointer())
    print("Size without tail pointer:", linkedlist.size_without_tail_pointer())

if __name__ == "__main__":
    main()