# Node class represents a single node in the linked list
class Node:
    # Initialize a new node with a value and optional next node reference
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # Return the value stored in this node
    def get_value(self):
        return self.value

    # Return the reference to the next node
    def get_next_node(self):
        return self.next_node

    # Set the reference to the next node
    def set_next_node(self, next_node):
        self.next_node = next_node

    # String representation of the node
    def __str__(self):
        return f"Node({self.value})"


# LinkedList class manages a collection of nodes
class LinkedList:
    # Initialize a new linked list with an optional starting value
    def __init__(self, value=None):
        self.head_node = Node(value)

    # Return the first node in the list
    def get_head_node(self):
        return self.head_node

    # Add a new node at the beginning of the list
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)  # Link new node to current head
        self.head_node = new_node  # Update head to new node

    # Add a new node at the end of the list
    def insert_end(self, value):
        new_node = Node(value)
        # Handle empty list case
        if self.head_node is None:
            self.head_node = new_node
            return

        # Find the last node in the list
        current_node = self.head_node
        while current_node.get_next_node() is not None:
            current_node = current_node.get_next_node()

        # Link the last node to our new node
        current_node.set_next_node(new_node)

    # Remove the first occurrence of a node with the specified value
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()

        # Special case: removing head node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            # Traverse list looking for the value to remove
            while current_node:
                next_node = current_node.get_next_node()
                if next_node and next_node.get_value() == value_to_remove:
                    current_node.set_next_node(
                        next_node.get_next_node()
                    )  # Skip over the removed node
                    current_node = None  # Exit the loop
                else:
                    current_node = next_node

    # Convert the linked list to a string representation
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        # Traverse the list and build string representation
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()

        return string_list


# Test the LinkedList implementation
ll = LinkedList("D")  # Create new list with 'D' as head
ll.insert_beginning("C")  # Add 'C' to the beginning
ll.insert_beginning("B")  # Add 'B' to the beginning
ll.insert_beginning("A")  # Add 'A' to the beginning
print(ll.stringify_list())  # Print the list: A->B->C->D

ll.remove_node("B")  # Remove node with value 'B'
print(ll.stringify_list())  # Print the modified list: A->C->D

# Code Explanation
