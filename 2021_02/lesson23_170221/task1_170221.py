# task1
"""
Write a program that reads in a sequence of characters and prints them in reverse order,
using your implementation of Stack.
"""
from collections import deque

my_sequence = ['a', 'b', 'c', 'd']

stack = deque()
print(f'Initial stack: {stack}')
for item in my_sequence:
    stack.append(item)
print(f'Stack after elements were added: {stack}')
print('Elements are poped from stack:')
while len(stack) > 0:
    print(stack.pop())
print('Stack after elements were poped:')
print(stack)
