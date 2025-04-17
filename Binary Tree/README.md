# 🌳 Binary Tree in Python

This project demonstrates a simple implementation of a **Binary Search Tree (BST)** in Python, encapsulated in a class `BinaryTree`. It supports key operations such as **insertion**, **deletion**, **search**, and **tree traversal** (in-order, pre-order, and post-order).

## 🚀 Features

- **Node-based structure**: Each node contains a value and pointers to its left and right children.
- **Insert element**: Adds a value into the BST following binary search rules.
- **Delete element**: Removes a value from the BST and re-balances if necessary.
- **Search element**: Checks whether a value exists in the tree.
- **Minimum and Maximum**: Retrieves the smallest and largest values in the tree.
- **Tree traversal**: Supports in-order, pre-order, and post-order traversals.

## 📦 Class: `BinaryTree`

### Methods

- **`__init__(self, root_value)`**: Initializes the tree with a root node containing `root_value`.
- **`insert_element(self, value)`**: Inserts `value` into the tree at the appropriate position.
- **`search_element(self, value)`**: Returns `True` if `value` exists in the tree, else `False`.
- **`delete_element(self, value)`**: Deletes the node with the given `value` from the tree.
- **`minimum_value(self)`**: Returns the smallest value in the tree.
- **`maximum_value(self)`**: Returns the largest value in the tree.
- **`inorder(self)`**: Returns a string representing an in-order traversal.
- **`preorder(self)`**: Returns a string representing a pre-order traversal.
- **`postorder(self)`**: Returns a string representing a post-order traversal.

## 📋 Example Usage

```python
if __name__ == "__main__":
    bt = BinaryTree(10)

    print("Binary Tree Example")

    # Insert elements
    bt.insert_element(5)
    bt.insert_element(15)
    bt.insert_element(2)
    bt.insert_element(7)
    bt.insert_element(12)
    bt.insert_element(20)

    # Display traversals
    print("\nTraversals after insertions:")
    print("In-order   :", bt.inorder())     # 2 5 7 10 12 15 20
    print("Pre-order  :", bt.preorder())    # 10 5 2 7 15 12 20
    print("Post-order :", bt.postorder())   # 2 7 5 12 20 15 10

    # Search elements
    print("\nSearching:")
    print("Search for 7  :", bt.search_element(7))
    print("Search for 100:", bt.search_element(100))

    # Minimum and maximum
    print("\nTree boundaries:")
    print("Minimum value:", bt.minimum_value())
    print("Maximum value:", bt.maximum_value())

    # Delete elements
    bt.delete_element(5)
    print("\nAfter deleting 5:")
    print("In-order:", bt.inorder())

    bt.delete_element(20)
    print("\nAfter deleting 20:")
    print("In-order:", bt.inorder())

    bt.delete_element(10)
    print("\nAfter deleting 10:")
    print("In-order:", bt.inorder())
```

### Output Example:

```
Binary Tree Example

Traversals after insertions:
In-order   : 2 5 7 10 12 15 20
Pre-order  : 10 5 2 7 15 12 20
Post-order : 2 7 5 12 20 15 10

Searching:
Search for 7  : True
Search for 100: False

Tree boundaries:
Minimum value: 2
Maximum value: 20

After deleting 5:
In-order: 2 7 10 12 15 20

After deleting 20:
In-order: 2 7 10 12 15

After deleting 10:
In-order: 2 7 12 15
