# 🧠 Static Array in Python

This project demonstrates a simple implementation of a **static array** in Python, encapsulated in a class `StaticArray`. The array has a fixed size and supports basic operations such as **insertion**, **deletion**, **display**, and **linear search**.

## 🚀 Features

- **Fixed-size array**: Simulates a static array with a size defined during initialization.
- **Insert element**: Adds an element at a specific index, only if that index is empty.
- **Delete element**: Removes an element from a specific index.
- **Linear search**: Searches for an element in the array.
- **Display array**: Prints the current state of the array with `None` for uninitialized positions.

## 📦 Class: `StaticArray`

### Methods

- **`__init__(self, size)`**: Initializes the array with the given `size`, setting all elements to `None`.
- **`display(self)`**: Prints the current state of the array. If an element is `None`, it prints `"None"`.
- **`insert_element(self, index, value)`**: Inserts a `value` at a given `index` in the array. If the index is out of bounds or the index is already occupied, it prints an error message.
- **`delete_element(self, index)`**: Deletes the element at the given `index` in the array. If the index is out of bounds or the element is already `None`, it prints an error message.
- **`linear_search(self, value)`**: Searches for a specific `value` in the array. If found, it returns the index; otherwise, it prints an error message and returns `-1`.

## 📋 Example Usage

```python
if __name__ == "__main__":
    SIZE = 5
    static_array = StaticArray(SIZE)

    print("Static Array Example")

    # Initial display of the array (empty)
    static_array.display()

    # Insert elements
    print("\nInserting random values:")
    for i in range(SIZE):
        value = random.randint(1, 100)
        static_array.insert_element(i, value)
    static_array.display()

    # Attempt to insert at an already occupied index
    static_array.insert_element(2, 999)  

    # Delete an element at a specific index
    print("\nDeleting element at index 2:")
    static_array.delete_element(2)
    static_array.display()

    # Search for a random element that exists in the array
    search_index = random.randint(0, SIZE - 1)
    search_value = static_array.array[search_index]
    print(f"\nSearching for the element {search_value} at index {search_index}:")
    static_array.linear_search(search_value)

    # Search for a value not present
    print("\nSearching for a value not present (999):")
    static_array.linear_search(999)

    # Final display of the array
    print("\nFinal array state:")
    static_array.display()
```

### Output Example:
```
Static Array Example
Array elements are:
None None None None None 

Inserting random values:
Inserting 54 at index 0
Inserting 22 at index 1
Inserting 83 at index 2
Inserting 15 at index 3
Inserting 77 at index 4
Array elements are:
54 22 83 15 77 

Inserting 999 at index 2
Index 2 already occupied. Use delete before inserting.

Deleting element at index 2 (83)
Array elements are:
54 22 None 15 77 

Searching for the element 15 at index 3:
Element 15 found at index 3

Searching for a value not present (999):
Element 999 not found

Final array state:
54 22 None 15 77 
