class queue:

    queue = []

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop(0)
    
    def print_queue(self):
        print(self.queue)
    
    def get_queue_size(self):
        return len(self.queue)
    
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.print_queue()
q.dequeue()
q.print_queue()
print(q.get_queue_size())
q.dequeue()
print(q.get_queue_size())

