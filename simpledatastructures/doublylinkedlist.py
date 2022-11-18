# Essentially: a doubly linked list allows traversal back and forth throughout the nodes

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        temp = Node(value)
        temp.next = self.head
        if self.head is not None:
            self.head.prev = temp
        self.head = temp

    def append(self, value):
        pointer = Node(value)
        pointer.next = None
        if self.head is None:
            pointer.prev = None
            self.head = pointer
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = pointer
        pointer.prev = last
        return

    def print_contents(self):
        top = self.head
        while top is not None:
            print(top.value)
            top = top.next


ll = DoublyLinkedList()
ll.push(12)
ll.append(33)
ll.append(44)
ll.push(77)
ll.print_contents()
