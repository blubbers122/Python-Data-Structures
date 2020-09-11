class Queue:
    def __init__(self, initial_value=[]):
        self.queue = initial_value

    def next(self):
        return self.queue.pop(0)

    def add(self, item):
        return self.queue.append(item)

    def print(self):
        print(self.queue)

queue = Queue([3,2,4,6,7])
queue.print()
queue.add(8)
queue.next()
queue.next()
queue.next()
queue.print()
