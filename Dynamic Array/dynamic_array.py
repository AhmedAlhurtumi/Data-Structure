import random

class DynamicArray:
    def __init__(self, initial_capacity=10):
        self.size = 0  # Current number of elements in the array
        self.capacity = initial_capacity  # Initial capacity
        self.array = [None] * self.capacity


    def display(self):
        print("Array elements are:")
        for i in range(self.size):
            if self.array[i] is None:
                print("None", end=" ")
            else:
                print(self.array[i], end=" ")
        print()

    def add(self, value):
        if self.size >= self.capacity:
            self.expand()
        self.array[self.size] = value
        self.size += 1
        print(f"Added {value} at index {self.size - 1}")

    def insert_element(self, index, value):
        if self.size >= self.capacity:
            self.expand()
        if index < 0 or index > self.size:
            print("Index out of bounds.")
            return
        if index < self.size:
            for i in range(self.size, index, -1):
                self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1
        print(f"Inserted {value} at index {index}")        

    def delete_element(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.size - 1] = None
                self.size -= 1
                print(f"Deleted {value} from index {i}")
                return
        print(f"{value} not found in the array.")

    def linear_search(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                print(f"Found {value} at index {i}")
                return i
        print(f"{value} not found in the array.")
        return -1

    def expand(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        print(f"Expanded array to capacity {self.capacity}")

    def shrink(self):
        if self.size <= self.capacity // 4:
            new_capacity = self.capacity // 2
            new_array = [None] * new_capacity
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
            self.capacity = new_capacity
            print(f"Shrunk array to capacity {self.capacity}")

    def is_empty(self):
        return self.size == 0
    
if __name__ == "__main__":
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

   