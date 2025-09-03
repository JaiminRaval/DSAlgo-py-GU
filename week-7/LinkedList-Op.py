# Define a Node class to represent each element in the LinkedList
class Node:
    def __init__(self, data=None):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    # Method to add a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty, new node becomes head
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to display the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    # Method to search for an element
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

# Demonstration of LinkedList operations
ll = LinkedList()
ll.append(10)  # Add element 10
ll.append(20)  # Add element 20
ll.append(30)  # Add element 30

print('Linked List:')
ll.display()  # Display list

print('Search for 20:', ll.search(20))  # Should return True
print('Search for 40:', ll.search(40))  # Should return False
