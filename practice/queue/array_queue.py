class Queue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
    
    def enqueue(self, value):
        if self.capacity == self.rear:
            print("The queue is full. Can't enqueue.")
            return
        
        self.queue[self.rear] = value
        self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("The queue is empty. Can't dequeue.")
            return None
        
        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        return value
    
    def empty(self):
        return self.front == self.rear
    
    def full(self):
        return self.capacity == self.rear