# Data-Structure
---

**Data Structure**:  
A way of organizing data so that it can be used effectively.

- Essential for creating fast and powerful algorithms.
- Help manage and organize data efficiently.
- Make code cleaner and easier to understand.

---

**Abstract Data Structure (ADS)**:  
An abstraction of data that defines the behavior and operations without specifying implementation details.

---

### **Examples**:

| Abstract Data Structure | Description                                 | Common Implementations      |
|-------------------------|---------------------------------------------|-----------------------------|
| Array                  | Collection of elements identified by index  | Static array, dynamic array |
| Stack                  | LIFO (Last In, First Out) structure          | Array, Linked List          |
| Queue                  | FIFO (First In, First Out) structure         | Array, Linked List          |
| Deque                  | Double-ended queue                           | Array, Doubly Linked List   |
| Linked List            | Sequence of nodes where each points to next | Singly, Doubly, Circular    |
| Tree                   | Hierarchical structure with parent-child     | Binary Tree, BST, Heap      |
| Graph                  | Set of nodes connected by edges              | Adjacency List, Matrix      |
| Hash Table             | Key-value pairs                              | Array with Hashing          |
| Set                    | Collection of unique elements                | Hash Table, BST             |
| Map / Dictionary       | Key-value mapping                            | Hash Table, Balanced Tree   |

---

## Complexity Analysis
---

### **Big-O Notation**  
Big-O Notation describes the **upper bound** of an algorithm’s time or space complexity in the **worst-case scenario**, helping to quantify performance as the input size (**n**) grows.

---

### **Purpose of Big-O**:

- Compares the efficiency of algorithms.
- Measures scalability rather than exact runtime.
- Ignores constants and focuses on growth rate.

---

### **Common Time Complexities**:

| Big-O        | Name                | Example                               |
|--------------|---------------------|----------------------------------------|
| O(1)         | Constant Time        | Accessing array element                |
| O(log n)     | Logarithmic Time     | Binary Search                          |
| O(n)         | Linear Time          | Linear Search, Traversing a list       |
| O(n log n)   | Linearithmic Time    | Merge Sort, Quick Sort (average case)  |
| O(n²)        | Quadratic Time       | Bubble Sort, Insertion Sort (worst)    |
| O(2ⁿ)        | Exponential Time     | Recursive Fibonacci                    |
| O(n!)        | Factorial Time       | Solving Traveling Salesman (brute-force)|

---

> 📌 **Note:** Big-O describes *worst-case*, but there are also **Big-Ω (Omega)** for *best-case* and **Big-Θ (Theta)** for *average-case* or tight bounds.

---

