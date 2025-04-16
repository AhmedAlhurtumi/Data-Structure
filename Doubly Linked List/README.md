# 🧠 Doubly Linked List in Python

This project demonstrates a **Doubly Linked List** implementation in Python. A doubly linked list allows for traversal in both directions (from head to tail and from tail to head), and supports basic operations like **insertion**, **deletion**, **searching**, and **displaying** elements.

## 🚀 Features

- **Insert at start**: Adds an element at the beginning of the list.
- **Insert at end**: Adds an element at the end of the list.
- **Delete**: Removes an element from the list (either from the start, middle, or end).
- **Search**: Finds an element in the list and returns its position.
- **Display**: Prints the elements of the list from head to tail.
- **Reverse display**: Prints the elements of the list from tail to head.
- **Check if empty**: Determines if the list is empty.

## 📦 Class: `DoublyLinkedList`

### Methods

- **`__init__(self)`**: Initializes an empty doubly linked list with `head` set to `None`.
- **`is_empty(self)`**: Returns `True` if the list is empty, otherwise `False`.
- **`insert_at_start(self, data)`**: Inserts a new element at the start of the list.
- **`insert_at_end(self, data)`**: Inserts a new element at the end of the list.
- **`delete(self, data)`**: Deletes the first occurrence of the given data in the list.
- **`search(self, value)`**: Searches for a value and returns its index if found.
- **`display(self)`**: Displays the elements of the list from head to tail.
- **`display_reverse(self)`**: Displays the elements of the list from tail to head.

## 📋 Example Usage

```python
dll = DoublyLinkedList()

print("\n--- Insertion ---")
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_start(5)
dll.insert_at_end(30)
dll.display()

print("\n--- Search ---")
dll.search(10)
dll.search(99)

print("\n--- Deletion ---")
dll.delete(5)
dll.display()

dll.delete(20)
dll.display()

dll.delete(99)  # Not found
dll.display()

print("\n--- Reverse Display ---")
dll.display_reverse()

print("\n--- Final State ---")
print("Is empty?", dll.is_empty())

```

### Output Example:

```output
--- Insertion ---
Inserted 10 at the end.
Inserted 20 at the end.
Inserted 5 at the beginning.
Inserted 30 at the end.
Doubly Linked List (Head to Tail):
5 <-> 10 <-> 20 <-> 30 <-> None

--- Search ---
Found 10 at position 1
99 not found in the list.

--- Deletion ---
Deleted 5 from the list.
Doubly Linked List (Head to Tail):
10 <-> 20 <-> 30 <-> None

Deleted 20 from the list.
Doubly Linked List (Head to Tail):
10 <-> 30 <-> None

99 not found in the list.
Doubly Linked List (Head to Tail):
10 <-> 30 <-> None

--- Reverse Display ---
Doubly Linked List (Tail to Head):
30 <-> 10 <-> None

--- Final State ---
Is empty? False
 
