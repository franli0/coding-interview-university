class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def value_at_with_tail_pointer(self, index):
        if index < 0:
            raise IndexError("Index is out of bounds")

        current_node = self.head
        for i in range(index):
            if current_node is None:
                raise IndexError("Index is out of bounds")
            current_node = current_node.next

        return current_node.data
    
    def value_at_without_tail_pointer(self, index):
        if index < 0:
            raise IndexError("Index is out of bounds")

        current_node = self.head
        counter = 0
        while counter < index and current_node is not None:
            current_node = current_node.next
            counter += 1

        if current_node is None:
            raise IndexError("Index is out of bounds")

        return current_node.data

def main():
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    linkedlist.head.next = Node(2)
    linkedlist.head.next.next = Node(3)
    print("Value at index 0 with tail pointer:", linkedlist.value_at_with_tail_pointer(0))
    print("Value at index 1 with tail pointer:", linkedlist.value_at_with_tail_pointer(1))
    print("Value at index 2 with tail pointer:", linkedlist.value_at_with_tail_pointer(2))

    print("Value at index 0 without tail pointer:", linkedlist.value_at_without_tail_pointer(0))
    print("Value at index 1 without tail pointer:", linkedlist.value_at_without_tail_pointer(1))
    print("Value at index 2 without tail pointer:", linkedlist.value_at_without_tail_pointer(2))

if __name__ == "__main__":
    main()