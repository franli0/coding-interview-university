class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def pop_front_with_tail_pointer(self):
        if self.head is None:
            return None
        node = self.head
        self.head = node.next

        if node is None:
            self.tail = None
        
        return node
    
    def erase_with_tail_pointer(self, index):
        if index < 0:
            raise ValueError("Index must be non-negative")

        if index == 0:
            return self.pop_front()

        node = self.head
        current_index = 1

        next_node = None

        while node is not None and current_index <= len(self):
            if current_index == index:
                break
            node = node.next
            current_index += 1

        if node is None:
            raise ValueError("Index is out of bounds")

        previous_node = node
        next_node = previous_node.next

        if self.tail is node:
            self.tail = previous_node

        if current_index == index:
            previous_node.next = next_node

            # Delete the node
            node.next = None

            return node

        return None
    
    def __len__(self):
        count = 0
        node = self.head
        while node is not None:
            node = node.next
            count += 1
        return count
    
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
    linkedlist.erase_with_tail_pointer(1)
    print(linkedlist)

if __name__ == "__main__":
    main()