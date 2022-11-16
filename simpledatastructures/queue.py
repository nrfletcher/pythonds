# The queue data structure
# Helpful for things such as task scheduling

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# Simple example of the Josephus algorithm
def flavius_josephus(people, interval):
    circle = Queue()
    for person in people:
        circle.enqueue(person)

    while circle.size() > 1:
        for i in range(interval):
            circle.enqueue(circle.dequeue())

        circle.dequeue()

    return circle.dequeue()
