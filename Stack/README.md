# 🧠 Stack in Python

This project demonstrates a simple implementation of a **stack** data structure in Python, encapsulated in a class `Stack`. The stack follows the **Last In, First Out (LIFO)** principle and supports basic stack operations such as **push**, **pop**, **peek**, **size**, **display**, and **clear**.

## 🚀 Features

- **Push element**: Adds an element to the top of the stack.
- **Pop element**: Removes and returns the top element of the stack.
- **Peek element**: Returns the top element of the stack without removing it.
- **Check if empty**: Determines if the stack is empty.
- **Size**: Returns the number of elements in the stack.
- **Display stack**: Displays the current state of the stack.
- **Clear stack**: Removes all elements from the stack.

## 📦 Class: `Stack`

### Methods

- **`__init__(self)`**: Initializes an empty stack.
- **`is_empty(self)`**: Returns `True` if the stack is empty, otherwise `False`.
- **`push(self, data)`**: Adds `data` to the top of the stack.
- **`pop(self)`**: Removes the top item from the stack. If the stack is empty, returns `"Stack is empty"`.
- **`peek(self)`**: Returns the top item without removing it. If the stack is empty, returns `"Stack is empty"`.
- **`size(self)`**: Returns the number of items in the stack.
- **`display(self)`**: Returns the current state of the stack or `"Stack is empty"` if the stack is empty.
- **`clear(self)`**: Removes all elements from the stack and returns `"Stack cleared"`.

## 📋 Example Usage

```python
if __name__ == "__main__":
    # Create a stack instance
    stack = Stack()

    # Display the initial state of the stack (should be empty)
    print("Initial stack:", stack.display())

    # Push items onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Display the stack after pushing items
    print("Stack after pushing items:", stack.display())

    # Peek the top item
    print("Top item of the stack:", stack.peek())

    # Pop an item from the stack
    stack.pop()
    print("Stack after popping an item:", stack.display())

    # Get the size of the stack
    print("Size of the stack:", stack.size())

    # Check if the stack is empty
    print("Is the stack empty?", stack.is_empty())

    # Clear the stack
    print(stack.clear())

    # Display the stack after clearing
    print("Stack after clearing:", stack.display())
