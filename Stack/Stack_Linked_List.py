# This is to implement Stack using Linked List
class node:
    
    data = None
    next = None

    def __init__(self):
        self.data = None
        self.next = None
    
    def add_data(self, data):
        self.data = data
    
    def add_next(self, node):
        self.next = node

class stack:

    head = None

    def __init__(self):
        self.head = None

    def add_head(self, node):
        self.head = node
    
    def push(self, node):
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = node
    
    def pop(self):
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next
        temp.next = None

    def print_stack(self):
        temp = self.head
        temp_list =  []
        while(temp.next != None):
            temp_list.append(temp.data)
            temp = temp.next
        temp_list.append(temp.data)
        print(temp_list)

n1 = node()
n1.add_data(1)
n2 = node()
n2.add_data(2)
n3 = node()
n3.add_data(3)
n4 = node()
n4.add_data(4)
n5 = node()
n5.add_data(5)
s = stack()
s.add_head(n1)
s.push(n2)
s.push(n3)       
s.push(n4)       
s.push(n5)
s.print_stack()
s.pop()
s.print_stack()
n6 = node()
n6.add_data(6)
s.push(n6)
s.print_stack()  
