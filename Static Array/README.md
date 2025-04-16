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
