class Array:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

def main():
    array = Array(100)
    if array.is_empty() == True:
        print("It's an empty array")
    else:
        print("It isn't an empty array")

if __name__ == "__main__":
    main()