import random

SIZE = 5
arr = [None] * SIZE


def display():
    print("Array elements are:")
    for i in range(SIZE):
        print(arr[i], end=" ")

def insert_element(index, value):
    if index < 0 or index >= SIZE:
        print("Index out of bounds")
        return
    
    print(f"Inserting {value} at index {index}")
    arr[index] = value

def delete_element(index):
    if index < 0 or index >= SIZE:
        print("Index out of bounds")
        return
    
    print(f"Deleting element at index {index}")
    arr[index] = None

def linear_search(value):
    for i in range(SIZE):
        if arr[i] == value:
            print(f"Element {value} found at index {i}")
            return i
    print(f"Element {value} not found")
    return -1

if __name__ == "__main__":
    print("Static Array Example")
    display()
    print("\n")
    # Insert elements
    for i in range(SIZE):
        insert_element(i, random.randint(1, 100))
    display()
    print("\n")
    # Delete an element
    delete_element(2)
    display()
    print("\n")
    # Search for an element
    search_value = random.randint(1, 100)
    print(f"Searching for {search_value}")
    linear_search(search_value)
    print("\n")
    # Final display of the array
    print("Final array state:")
    display()
    print("\n")
    
