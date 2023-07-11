def jump_to_index(array, index):
    current_index = 0
    while current_index < index:
        current_index += 1
    return array[current_index]

def main():
    array = [1,2,3,4,5,6,7]
    index = 4
    value = jump_to_index(array, index)
    print(value)

if __name__ == "__main__":
  main()