int[] array = new int[100];

// Get the pointer to the first element in the array.
int* pointer = array;

// Calculate the pointer to the element at index 51.
pointer += 51;

// Dereference the pointer to get the value of the element at index 5.
int value = *pointer;