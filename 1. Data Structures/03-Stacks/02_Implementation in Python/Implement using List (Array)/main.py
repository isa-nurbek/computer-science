class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.items = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item from the stack
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        # Return the top item from the stack without removing it
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def __str__(self):
        # Return a string representation of the stack
        return str(self.items)


# Example usage
if __name__ == "__main__":
    stack = Stack()

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushes:", stack)  # Output: [10, 20, 30]

    # Pop an element from the stack
    print("Popped:", stack.pop())  # Output: 30
    print("Stack after pop:", stack)  # Output: [10, 20]

    # Peek at the top element
    print("Top element:", stack.peek())  # Output: 20

    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())  # Output: False

    # Get the size of the stack
    print("Stack size:", stack.size())  # Output: 2
