# creating an empty stack using a list/Array in py
stack = []

# Push items onto the stack using .append()
stack.append(10)  # Stack: [10]
stack.append(20)  # Stack: [10, 20]
stack.append(30)  # Stack: [10, 20, 30]

# peek at the top item
print("Top item:", stack[-1])  # Output: 30

# pop items from the stack using .pop()
print("Popped:", stack.pop())  # Output: 30, Stack: [10, 20]
print("Popped:", stack.pop())  # Output: 20, Stack:

# check if stack is empty or not (returns bool)
print("Is empty?", len(stack) == 0)  # Output: False
