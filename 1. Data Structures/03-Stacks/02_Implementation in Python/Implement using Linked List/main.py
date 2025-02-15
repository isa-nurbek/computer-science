# Node class represents an element in the stack
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node (initially None)


# Stack class implements a stack using a linked list
class Stack:
    def __init__(self):
        self.top = None  # Top of the stack (initially None)

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Push a new element onto the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.top  # Link the new node to the current top
        self.top = new_node  # Update the top to the new node

    # Remove and return the top element from the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")  # Raise error if stack is empty
        popped_data = self.top.data  # Get data from the top node
        self.top = self.top.next  # Move the top to the next node
        return popped_data  # Return the popped data

    # Return the top element without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")  # Raise error if stack is empty
        return self.top.data  # Return the data of the top node

    # String representation of the stack for easy visualization
    def __str__(self):
        if self.is_empty():
            return "Stack is empty"  # Return message if stack is empty
        current = self.top  # Start from the top
        stack_str = ""  # Initialize an empty string
        while current:
            stack_str += str(current.data) + " -> "  # Append current node data
            current = current.next  # Move to the next node
        return stack_str[:-4]  # Remove the last " -> " for cleaner output


# Example usage of the Stack class
stack = Stack()  # Create a new stack

stack.push(10)  # Push 10 onto the stack
stack.push(20)  # Push 20 onto the stack
stack.push(30)  # Push 30 onto the stack

print(stack)  # Output: 30 -> 20 -> 10 (Last In, First Out order)

print("Popped:", stack.pop())  # Output: Popped: 30 (removes top element)
print(stack)  # Output: 20 -> 10 (Stack after popping 30)

print("Top element:", stack.peek())  # Output: Top element: 20 (peek at the top)

stack.push(40)  # Push 40 onto the stack
print(stack)  # Output: 40 -> 20 -> 10 (40 is now the new top)

"""
Output:

30 -> 20 -> 10
Popped: 30
20 -> 10
Top element: 20
40 -> 20 -> 10

"""

# Big O:

"""
## Time and Space Complexity Analysis:

"""


# ********************************************************************************************************************* #

# Code Explanation:

"""


"""
