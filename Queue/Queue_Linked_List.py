# This is to implement Queue data structure using Linked Lists.
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
    
class queue:

    head = None

    def __init__(self):
        self.head = None
    
    def add_head(self, node):
        self.head = node
    
    def enqueue(self, node):
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = node

    def dequeue(self):
        self.head = self.head.next

    def print_queue(self):
        temp = self.head
        temp_list = []
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
q = queue()
q.add_head(n1)
q.enqueue(n2)
q.enqueue(n3)
q.enqueue(n4)
q.enqueue(n5)
q.print_queue()
q.dequeue()
q.print_queue()
q.dequeue()
q.print_queue()
n6 = node()
n6.add_data(6)
q.enqueue(n6)
q.print_queue()
