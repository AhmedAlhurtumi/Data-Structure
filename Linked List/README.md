# 🧠 Linked List in Python

This project demonstrates a simple implementation of a **singly linked list** in Python, encapsulated in a class `LinkedList`. The linked list supports various operations such as **insertion**, **deletion**, **search**, and **display**.

## 🚀 Features

- **Insert at start**: Adds an element at the beginning of the list.
- **Insert at end**: Adds an element at the end of the list.
- **Delete element**: Removes a specific element from the list.
- **Search for element**: Finds an element in the list and returns its index.
- **Display list**: Prints all elements in the list.
- **Check if empty**: Determines if the list is empty.

## 📦 Class: `LinkedList`

### Methods

- **`__init__(self)`**: Initializes the linked list with an empty list.
- **`is_empty(self)`**: Returns `True` if the list is empty, otherwise `False`.
- **`insert_at_start(self, data)`**: Inserts an element at the beginning of the list.
- **`insert_at_end(self, data)`**: Inserts an element at the end of the list.
- **`delete(self, data)`**: Deletes the first occurrence of a specified element.
- **`search(self, data)`**: Searches for an element in the list and returns its index if found.
- **`display(self)`**: Prints all elements in the list in a human-readable format.

## 📋 Example Usage

```python
if __name__ == "__main__":
    ll = LinkedList()

    print("\n--- Insertion ---")
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_start(5)
    ll.display()

    print("\n--- Search ---")
    ll.search(10)
    ll.search(99)

    print("\n--- Deletion ---")
    ll.delete(5)
    ll.display()

    ll.delete(20)
    ll.display()

    ll.delete(99)  # Not found
    ll.display()

    print("\n--- Final State ---")
    print("Is empty?", ll.is_empty())

```
### Output Example:
```
--- Insertion ---
Inserted 10 as the first element.
Inserted 20 at the end of the list.
Inserted 5 at the start of the list.
Linked List elements:
5 -> 10 -> 20 -> None

--- Search ---
Found 10 at index 1.
99 not found in the list.

--- Deletion ---
Deleted 5 from the list.
Linked List elements:
10 -> 20 -> None
Deleted 20 from the list.
Linked List elements:
10 -> None
99 not found in the list.
Linked List elements:
10 -> None

--- Final State ---
Is empty? False

