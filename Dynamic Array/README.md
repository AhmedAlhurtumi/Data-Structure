# 🧠 Dynamic Array in Python

This project demonstrates a **dynamic array** implementation in Python, where the array expands or shrinks based on the number of elements it holds. The dynamic array supports basic operations like **adding**, **inserting**, **deleting**, **searching**, and **displaying** the elements.

## 🚀 Features

- **Dynamic resizing**: Automatically expands when the capacity is reached and shrinks when elements are deleted.
- **Insert element**: Adds an element at a specific index.
- **Delete element**: Removes an element from the array.
- **Linear search**: Searches for an element in the array.
- **Display array**: Prints the current state of the array.
- **Check if empty**: Determines if the array is empty.

## 📦 Class: `DynamicArray`

### Methods

- **`__init__(self, initial_capacity=10)`**: Initializes the dynamic array with a given initial capacity. If the capacity is not provided, the default is set to 10.
- **`display(self)`**: Prints the elements of the dynamic array.
- **`add(self, value)`**: Adds a value at the end of the array. Expands the array if necessary.
- **`insert_element(self, index, value)`**: Inserts a value at the specified index and expands the array if necessary.
- **`delete_element(self, value)`**: Deletes the first occurrence of the value in the array.
- **`linear_search(self, value)`**: Searches for a value and returns its index if found.
- **`expand(self)`**: Expands the array when the capacity is exceeded by doubling the array's size.
- **`shrink(self)`**: Shrinks the array when the number of elements is less than a quarter of the capacity.
- **`is_empty(self)`**: Returns `True` if the array is empty, otherwise `False`.

## 📋 Example Usage

```python
print("Initializing dynamic array...")
da = DynamicArray(initial_capacity=4)  # Start with small capacity to force expansion

# Display empty state
print("\n--- Initial State ---")
da.display()
print("Is empty?", da.is_empty())

# Add elements to fill capacity
print("\n--- Adding Elements ---")
for val in [10, 20, 30, 40]:
    da.add(val)
da.display()

# Add one more to trigger expansion
print("\n--- Triggering Expansion ---")
da.add(50)
da.display()

# Insert at the beginning
print("\n--- Insert at Beginning ---")
da.insert_element(0, 5)
da.display()

# Insert in the middle
print("\n--- Insert in Middle ---")
da.insert_element(3, 25)
da.display()

# Insert at the end
print("\n--- Insert at End ---")
da.insert_element(da.size, 60)
da.display()

# Invalid insert (out of bounds)
print("\n--- Insert Out of Bounds ---")
da.insert_element(999, 999)
da.display()

# Search for existing and non-existing elements
print("\n--- Linear Search ---")
da.linear_search(25)  # Should be found
da.linear_search(99)  # Should not be found

# Delete existing element
print("\n--- Delete Existing Element ---")
da.delete_element(25)
da.display()

# Delete non-existing element
print("\n--- Delete Non-existing Element ---")
da.delete_element(99)
da.display()

# Trigger shrinking by deleting multiple elements
print("\n--- Trigger Shrinking ---")
da.delete_element(5)
da.delete_element(10)
da.delete_element(20)
da.delete_element(30)
da.delete_element(40)
da.shrink()
da.display()

# Final state and checks
print("\n--- Final State ---")
da.display()
print("Size:", da.size)
print("Capacity:", da.capacity)
print("Is empty?", da.is_empty())
