# Recemmended queue code for py
from collections import deque
# Create a queue using deque (more efficient)
queue = deque()
# Add items
queue.append("Apple")
queue.append("Banana")
queue.append("Cherry")
print(f"Queue: {list(queue)}")
# Remove items (FIFO - First In, First Out)
first_item = queue.popleft()
print(f"Removed: {first_item}")
print(f"Queue now: {list(queue)}")
# Check what's next without removing
print(f"Next item: {queue[0]}")







# another approach
class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add item to the back of the queue"""
        self.queue.append(item)
        print(f"Added: {item}")

    def dequeue(self):
        """Remove and return item from the front of the queue"""
        if self.is_empty():
            return "Queue is empty!"
        item = self.queue.pop(0)
        print(f"Removed: {item}")
        return item

    def peek(self):
        """Look at the front item without removing it"""
        if self.is_empty():
            return "Queue is empty!"
        return self.queue[0]

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue"""
        return len(self.queue)

    def display(self):
        """Show all items in the queue"""
        print(f"Queue: {self.queue}")

# Example usage
print("=== Queue Demo ===")
q = SimpleQueue()

# Add items (enqueue)
q.enqueue("First")
q.enqueue("Second")
q.enqueue("Third")
q.display()

# Look at front item
print(f"Front item: {q.peek()}")

# Remove items (dequeue)
q.dequeue()
q.dequeue()
q.display()

print(f"Queue size: {q.size()}")
