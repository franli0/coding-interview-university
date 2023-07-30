class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_back_with_tail_pointer(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        if self.tail is None:
            self.tail = new_node
            return

        node = self.head

        while node.next is not None:
            node = node.next

        node.next = new_node
        self.tail = new_node
                

    def push_back_without_tail_pointer(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            
            node.next = new_node


    def __str__(self):
        string = ""
        node = self.head
        while node is not None:
            string += str(node.data) + " "
            node = node.next

        return string.strip()

def main():
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    linkedlist.head.next = Node(2)
    linkedlist.head.next.next = Node(3)
    linkedlist.push_back_with_tail_pointer(4)
    linkedlist.push_back_with_tail_pointer(5)
    linkedlist.push_back_with_tail_pointer(6)
    print(linkedlist)
    
    linkedlist = LinkedList()
    linkedlist.head = Node(7)
    linkedlist.head.next = Node(8)
    linkedlist.head.next.next = Node(9)
    linkedlist.push_back_without_tail_pointer(10)
    linkedlist.push_back_without_tail_pointer(11)
    linkedlist.push_back_without_tail_pointer(12)
    print(linkedlist)

if __name__ == "__main__":
    main()