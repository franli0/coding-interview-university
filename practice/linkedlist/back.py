class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def back_with_tail_pointer(self):
        node = self.head
        if node is None:
            return None
        
        if node == self.tail:
            self.tail = node
        
        while node.next is not None:
            node = node.next

        return node.data
    
    def back_without_tail_pointer(self):
        node = self.head
        if node is None:
            return None
        
        while node.next is not None:
            node = node.next

        return node.data

def main():
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    linkedlist.head.next = Node(2)
    linkedlist.head.next.next = Node(3)
    print("Back of linked list with tail pointer", linkedlist.back_with_tail_pointer())
    print("Back of linked list without tail pointer", linkedlist.back_without_tail_pointer())

if __name__ == "__main__":
    main()