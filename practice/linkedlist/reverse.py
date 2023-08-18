class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def reverse_with_tail_pointer(self):
          current = self.head
          previous = None
          while current is not None:
              next_node = current.next
              current.next = previous
              previous = current
              current = next_node

          self.head = previous
          self.tail = current

          print(self.head)
          return self.head
    
    # def __iter__(self):
    #     node = self.head
    #     while node is not None:
    #         yield node
    #         node = node.next

def main():
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    linkedlist.head.next = Node(2)
    linkedlist.head.next.next = Node(3)
    print(linkedlist.reverse_with_tail_pointer())

if __name__ == "__main__":
    main()