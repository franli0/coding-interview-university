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
    
    def insert_with_tail_pointer(self, index, value):
        if index < 0:
            raise ValueError("Index must be non-negative")

        if index == 0:
            return self. push_front_with_tail_pointer(value)

        node = self.head
        current_index = 0

        while node is not None and current_index < index - 1:
            node = node.next
            current_index += 1

        if node is None:
            raise ValueError("Index is out of bounds")

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

        if node is self.tail:
            self.tail = new_node

        return new_node

    def insert_without_tail_pointer(self, index, value):
        if index < 0:
            raise ValueError("Index must be non-negative")
        
        if index == 0:
            return self.push_front_without_tail_pointer(value)
        
        node = self.head
        current_index = 0
        while node is not None and current_index < index - 1:
            node = node.next
            current_index += 1
        
        if node is None:
            raise ValueError("Index is out of bounds")
        
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

        return new_node
    
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
    linkedlist.insert_with_tail_pointer(3, 4)
    print(linkedlist)

if __name__ == "__main__":
    main()