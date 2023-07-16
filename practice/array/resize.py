class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    def pop(self):
        if self.is_empty():
            raise Exception("The array is empty")
        
        self.size -= 1
        item = self.data[self.size]
        self.data[self.size] = None

        if self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)
        
        return item, self.size
    
    def prepend(self, item):
        if self.is_full():
            self.resize(2 * self.capacity)
        
        if self.is_empty():
            self.data[0] = item
        else:
            for i in range(self.size, 0, -1):
                self.data[i] = self.data[i - 1]
            
            self.data[0] = item

        self.size += 1
    
    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        
        self.data = new_data
        self.capacity = new_capacity
        return self.data, self.capacity

    def __repr__(self):
        return str(self.data[:self.size])

def main():
    array = Array(100)
    for i in range(1, 101):
        array.prepend(i)
    print(array.resize(200))
    print(array)
    
if __name__ == "__main__":
    main()