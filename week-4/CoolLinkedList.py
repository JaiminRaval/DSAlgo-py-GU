# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create individual nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link the nodes together
node1.next = node2
node2.next = node3
# node3.next is already None (end of list)

# Function to traverse and print the linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Function to insert a new node at the beginning
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  # new_node becomes the new head

# Print original list
print("Original list:")
print_list(node1)  # Output: 10 -> 20 -> 30 -> None

# Insert at beginning
head = insert_at_beginning(node1, 5)
print("After inserting 5 at beginning:")
print_list(head)   # Output: 5 -> 10 -> 20 -> 30 -> None
