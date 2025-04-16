class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} as the first element.")
            return
        
        current_node = self.head 
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node
        print(f"Inserted {data} at the end.")

    def delete(self, data):
        if self.is_empty():
            print("List is empty.")
            return
        
        # Case 1: Deleting the head node
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            print(f"Deleted {data} from the list.")
            return
        
        # Case 2: Deleting a non-head node
        current_node = self.head 
        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            print(f"{data} not found in the list.")
            return
        
        if current_node.next:
            current_node.next.prev = current_node.prev

        if current_node.prev:
            current_node.prev.next = current_node.next
    
        print(f"Deleted {data} from the list.")

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                print(f"Found {value} at position {index}")
                return index
            current = current.next
            index += 1
        print(f"{value} not found in the list.")
        return -1
    
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        print("Doubly Linked List (Head to Tail):")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_reverse(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current.next:
            current = current.next
        print("Doubly Linked List (Tail to Head):")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


if __name__ == "__main__":
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
