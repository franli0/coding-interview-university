class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue peek:", queue.peek())

if __name__ == "__main__":
    main()