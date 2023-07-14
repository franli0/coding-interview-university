class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_full(self):
        return len(self.items) == self.capacity
    
    def push(self, item):
        if self.is_full():
            raise Exception("The array is full")
        self.items.append(item)

    def __str__(self):
        return str(self.items)

def main():
    array = Array(100)
    for i in range(1, 11):
        array.push(i)
    print(array)

if __name__ == "__main__":
    main()