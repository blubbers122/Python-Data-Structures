class Stack:
    def __init__(self, initial_value=[]):
        self.stack = initial_value

    def pop(self):
        return self.stack.pop(-1)

    def push(self, item):
        self.stack.append(item)
        return self.stack

    def print(self):
        print(self.stack)

stack = Stack([1,3,4,5,6,8])
stack.pop()
stack.push(24)
stack.print()
