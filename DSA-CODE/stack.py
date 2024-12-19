"""
Stack is a class that encapsulates the stack operations.
is_empty checks if the stack is empty
push adds an item to the top of the stack.
pop removes and returns the top item from the stack.
peek returns the top item withut removing it.
size returns the number of elements in the stack.
"""
# Create an empty stach
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Check if the stack is empty
is_empty = len(stack) == 0

# Peek at the top element without removing it
top_element = stack[-1]

print(stack)
print(is_empty)
print(top_element)