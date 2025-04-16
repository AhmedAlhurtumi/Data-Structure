class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the start of the list.")

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
        print(f"Inserted {data} at the end of the list.")

    def delete(self, data):
        if self.head is None:
            print("List is empty.")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            print(f"Deleted {data} from the list.")
            return
        
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next is None:
            print(f"{data} not found in the list.")
            return
        
        current_node.next = current_node.next.next
        print(f"Deleted {data} from the list.")

    def search(self, data):
        current_node = self.head
        index = 0 
        while current_node:
            if current_node.data == data:
                print(f"Found {data} at index {index}.")
                return index
            current_node = current_node.next
            index += 1
        print(f"{data} not found in the list.")
        return -1
    
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        
        current_node = self.head
        print("Linked List elements:")
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

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
