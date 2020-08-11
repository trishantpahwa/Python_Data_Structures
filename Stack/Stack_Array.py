# This data structure is a stack using array or a list.
# The link to the video: https://youtu.be/ZsQ34X2N6l0
class stack:

    stack = []

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def print_stack(self):
        print(self.stack)

    def get_stack_size(self):
        return len(self.stack)

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.print_stack()
print(s.get_stack_size())
s.pop()
s.pop()
s.print_stack()
print(s.get_stack_size())
