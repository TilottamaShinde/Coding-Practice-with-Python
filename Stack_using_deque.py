#Implementation of stack using deque

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item);
        print(f"Pushed {item} into stack")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def pick(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def display(self):
        print("Stack (Top -> Bottom) : ", list(reversed(self.stack)))


#Example
stack = Stack()
stack.push('A')
stack.push('B')
stack.push('C')

stack.display()

print("Popped element : ",stack.pop())
stack.display()
print("Top element : ", stack.pick())