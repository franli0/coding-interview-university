class Array:
    def __init__(self, data):
        self.data = data
    
    def at(self, index):
        if index < 0 or index >= len(self.data):
            raise Exception("Index out of bounds")
        return self.data[index]
    
def main():
    array = Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(array.at(2))
    print(array.at(100))

if __name__ == "__main__":
    main()