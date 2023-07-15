class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0
    
    def prepend(self, item):
        if self.is_full():
            raise Exception("The array is full")
        
        if self.is_empty():
            self.data[0] = item
        else:
            for i in range(self.size, 0, -1):
                self.data[i] = self.data[i - 1]
            
            self.data[0] = item

        self.size += 1
    
    def delete(self, index):
        if self.is_empty():
            raise Exception("The array is empty")
        
        self.size -= 1
        item = self.data[index]
        self.data[index] = None
        for i in range(index, self.size):
            self.data[i] =  self.data[i+1]

        return item
    
    def __repr__(self):
        return str(self.data[:self.size])

def main():
    array = Array(100)
    array.prepend(1)
    array.prepend(2)
    array.prepend(3)
    array.prepend(4)
    array.prepend(5)
    deleted = array.delete(0)
    print(deleted)
    print(array)

if __name__ == "__main__":
    main()