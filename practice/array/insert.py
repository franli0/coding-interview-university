class Array:
    def __init__(self, capacity):
        self.data = [None] * capacity

    def insert(self, index, item):
        if index < 0 or index > len(self.data):
            raise Exception("Index out of bounds")
        
        for i in range(len(self.data) - 1, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = item

def main():
    array = Array(100)
    array.insert(0, 1)
    array.insert(1, 2)
    array.insert(2, 3)
    print(array.data)

if __name__ == "__main__":
    main()