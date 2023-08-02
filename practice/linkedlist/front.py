class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def front_with_tail_pointer(self):
        if self.head is not None:
            if self.tail is None:
                self.tail = self.head

            return self.tail.data

        else:
            return None
    
    def front_without_tail_pointer(self):
        node = self.head
        if node is None:
            return None
        
        return node.data
        
def main():
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    linkedlist.head.next = Node(2)
    linkedlist.head.next.next = Node(3)
    print(linkedlist.front_with_tail_pointer())
    print(linkedlist.front_without_tail_pointer())

if __name__ == "__main__":
  main()