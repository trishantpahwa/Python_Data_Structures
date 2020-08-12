# This is an implementation of linked lists.
# Since, it is a dynamic data structure, we will use a sub component called node.
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

class linked_list:

    head = None

    def __init__(self):
        self.head = None

    def add_head(self, node):
        self.head = node

    def add_node(self, node):
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = node
    
    def remove_node(self, position):  # Position starts from 0 <- Head
        if position == 0:
            self.head = self.head.next
        else:
            index = 1
            temp = self.head
            while(temp.next.next != None and index < position):
                temp = temp.next
                index += 1
            if index == position:
                temp.next = temp.next.next
            else:
                temp.next = None

    def print_linked_list(self):
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
n6 = node()
n6.add_data(6)
n7 = node()
n7.add_data(7)
n8 = node()
n8.add_data(8)
n9 = node()
n9.add_data(9)
n10 = node()
n10.add_data(10)
ll = linked_list()
ll.add_head(n1)
ll.add_node(n2)
ll.add_node(n3)
ll.add_node(n4)
ll.add_node(n5)
ll.add_node(n6)
ll.add_node(n7)
ll.add_node(n8)
ll.print_linked_list()
ll.remove_node(1)
ll.print_linked_list()
ll.remove_node(3)
ll.print_linked_list()
ll.add_node(n9)
ll.add_node(n10)
ll.print_linked_list()