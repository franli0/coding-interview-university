class Array:
    def __init__(self, items):
        self.items = items
    
    def size(self):
        return len(self.items)
    
def main():
    array = Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(array.size())

if __name__ == "__main__":
    main()