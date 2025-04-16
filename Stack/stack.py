class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            return "Stack is empty"
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
    
    def size(self):
        return len(self.stack)

    def display(self):
        if not self.is_empty():
            return self.stack
        else:
            return "Stack is empty"
        
    def clear(self):
        self.stack.clear()
        return "Stack cleared"
    
# Example usage
if __name__ == "__main__":
    # Create a stack instance
    stack = Stack()

    # Display the initial state of the stack (should be empty)
    print("Initial stack:", stack.display())

    # Push items onto the stack
    print("Pushing 10 onto stack")
    stack.push(10)
    print("Pushing 20 onto stack")
    stack.push(20)
    print("Pushing 30 onto stack")
    stack.push(30)

    # Display the stack after pushing items
    print("Stack after pushing items:", stack.display())

    # Peek the top item
    print("Top item of the stack:", stack.peek())

    # Pop an item from the stack
    print("Popping an item from the stack...") 
    stack.pop()
    print("Stack after popping an item:", stack.display())

    # Get the size of the stack
    print("Size of the stack:", stack.size())

    # Check if the stack is empty
    print("Is the stack empty?", stack.is_empty())

    # Clear the stack
    print("Clearing the stack...")
    print(stack.clear())

    # Display the stack after clearing
    print("Stack after clearing:", stack.display())
 