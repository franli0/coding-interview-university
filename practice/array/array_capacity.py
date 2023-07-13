class Array:
    
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def capacity(self):
        return self.capacity

    def is_full(self):
        return len(self.data) == self.capacity

    def is_empty(self):
        return len(self.data) == 0

    def append(self, value):
        if self.is_full():
            raise Exception("Array is full")
        self.data.append(value)

    def remove(self, index):
        if index < 0 or index >= len(self.data):
            raise Exception("Index out of range")
        self.data.pop(index)

def main():
    array = Array(100)
    print(array.capacity)

if __name__ == "__main__":
    main()