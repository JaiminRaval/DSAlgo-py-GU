# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None  # Points to the top node (head of linked list)
        self.size = 0    # Keep track of stack size

    def push(self, data):
        """Add an element to the top of the stack"""
        new_node = Node(data)
        new_node.next = self.top  # Point new node to current top
        self.top = new_node       # Make new node the top
        self.size += 1
        print(f"Pushed {data} to stack")

    def pop(self):
        """Remove and return the top element"""
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None

        popped_data = self.top.data
        self.top = self.top.next  # Move top to next node
        self.size -= 1
        print(f"Popped {popped_data} from stack")
        return popped_data

    def peek(self):
        """View the top element without removing it"""
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        return self.top.data

    def is_empty(self):
        """Check if stack is empty"""
        return self.top is None

    def get_size(self):
        """Get the current size of stack"""
        return self.size

    def display(self):
        """Display all elements in the stack (top to bottom)"""
        if self.is_empty():
            print("Stack is empty!")
            return

        print("Stack (top to bottom):", end=" ")
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()

    # Test pushing elements
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Display current stack
    stack.display()  # Output: 30 -> 20 -> 10 -> None

    # Test peek
    print(f"Top element: {stack.peek()}")  # Output: 30

    # Test popping elements
    stack.pop()  # Removes 30
    stack.pop()  # Removes 20

    stack.display()  # Output: 10 -> None

    # Check size and if empty
    print(f"Stack size: {stack.get_size()}")  # Output: 1
    print(f"Is empty: {stack.is_empty()}")    # Output: False

    # Pop remaining element
    stack.pop()  # Removes 10
    print(f"Is empty: {stack.is_empty()}")    # Output: True
