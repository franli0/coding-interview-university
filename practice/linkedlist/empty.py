class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def empty_with_tail_pointer(self):
        return self.head is None
    
    def empty_without_tail_pointer(self):
        return self.head is None and self.tail is None

def main():
    linkedlist = LinkedList()
    print("Is empty with tail pointer:", linkedlist.empty_with_tail_pointer())
    print("Is empty without tail pointer:", linkedlist.empty_without_tail_pointer())

    linkedlist.head = Node(1)
    print("Is empty with tail pointer:", linkedlist.empty_with_tail_pointer())
    print("Is empty without tail pointer:", linkedlist.empty_without_tail_pointer())

if __name__ == "__main__":
    main()