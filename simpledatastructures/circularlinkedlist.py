# A circular linked list is a linked list where the tail node points to the head node as opposed to null or None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.value = data

    def set_next(self, nxt):
        self.next = nxt


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        pointer = Node(value)
        temp = self.head
        pointer.set_next(self.head)

        if self.head is not None:
            while(temp.get_next() != self.head):
                temp = temp.get_next()
            temp.set_next(pointer)
        else:
            pointer.set_next(pointer)
        self.head = pointer


circular = CircularLinkedList()
circular.add(22)
circular.add(23)
circular.add(26)
circular.add(29)

temp = circular.head
for i in range(10):
    print(temp.get_next())
    temp = temp.get_next()
