# The deque (double ended queue) data structure
# Combines the functionality of a stack and queue, and it's implementation is up to the programmer

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def palindrome_checker(word):
    deque = Deque()
    for i in word:
        deque.add_front(i)

    flipped = ''
    while not deque.is_empty():
        flipped += deque.remove_front()

    return word == flipped


def palindrome_two_pointers(word):
    deque = Deque()

    for i in word:
        deque.add_rear(i)

    same = True

    while deque.size() > 1 and same:
        front = deque.remove_front()
        rear = deque.remove_rear()
        if front != rear:
            same = False

    return same
