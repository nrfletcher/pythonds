# The linked list is a list with references to nearby data via an internal structure known as a node
# Nodes hold references to either the next value (singly linked list) or both prior and next (doubly linked)
# There are also circular singly and doubly linked lists which has the last node point to the first node, to wrap

class Node:
    def __init__(self, initial):
        self.data = initial
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, nxt):
        self.next = nxt


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, value):
        temp = Node(value)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        curr = self.head
        count = 0

        while curr is not None:
            count += 1
            curr = curr.get_next()

        return count

    def search(self, value):
        curr = self.head
        found = False
        while curr is not None and not found:
            if curr.get_data() == value:
                found = True
            else:
                curr = curr.get_next()

        return found

    def remove(self, value):
        curr = self.head
        previous = None
        found = False

        while not found:
            if curr.get_data() == value:
                found = True
            else:
                previous = curr
                curr = curr.get_next()

        if previous is None:
            self.head = curr.get_next()
        else:
            previous.set_next(curr.get_next())


class OrderedSinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        curr = self.head
        count = 0

        while curr is not None:
            count += 1
            curr = curr.get_next()

        return count

    def search(self, value):
        curr = self.head
        found = False
        stop = False
        while curr is not None and found and not stop:
            if curr.get_next() == value:
                found = True
            else:
                if curr.get_data() > value:
                    stop = True
                else:
                    curr = curr.get_next()

        return found

    def add(self, value):
        curr = self.head
        previous = None
        stop = False

        while curr is not None and not stop:
            if curr.get_data() > value:
                stop = True
            else:
                previous = curr
                curr = curr.get_next()

        temp = Node(value)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(curr)
            previous.set_next(temp)


def merged_lists(l1, l2):
    l3 = SinglyLinkedList()

    l3.add(l1.head)
    l3.add(l2.head)

    temp1 = l1.head
    while temp1 is not None:
        l3.add(temp1.get_data())
        temp1 = temp1.get_next()

    temp2 = l2.head
    while temp2 is not None:
        l3.add(temp2.get_data())
        temp2 = temp2.get_next()

    return l3


def print_list_contents(ll):
    temp = ll.head
    while temp is not None:
        print(temp.get_data())
        temp = temp.get_next()


def merged_list_ordered(l1, l2):
    l3 = OrderedSinglyLinkedList()

    l3.add(l1.head)
    l3.add(l2.head)

    temp1 = l1.head
    while temp1 is not None:
        l3.add(temp1.get_data())
        temp1 = temp1.get_next()

    temp2 = l2.head
    while temp2 is not None:
        l3.add(temp2.get_data())
        temp2 = temp2.get_next()

    return l3


def list_builder():
    ll_type = int(input('What type? Respond with "0" for unordered and "1" for ordered'))
    ll = None
    type_str = ''

    if ll_type == 1:
        ll = OrderedSinglyLinkedList()
        type_str = 'Ordered'
    elif ll_type == 0:
        ll = SinglyLinkedList()
        type_str = 'Unordered'
    else:
        print('Invalid response')
        return 0

    print(type_str)
    end = False
    while not end:
        val = input('Value: ')
        if type(val) is not int:
            end = True
            continue
        ll.add(int(val))

    print('List built')
    return ll


def list_tests():
    l1 = SinglyLinkedList()
    l1.add(22)
    l1.add(33)
    l1.add(44)

    l2 = SinglyLinkedList()
    l2.add(77)
    l2.add(88)
    l2.add(99)

    l4 = SinglyLinkedList()
    l4.add(123)
    l4.add(345)
    l4.add(22)

    l5 = SinglyLinkedList()
    l5.add(90)
    l5.add(45)
    l5.add(333)

    l6 = merged_lists(l4, l5)
    l3 = merged_lists(l1, l2)

    print_list_contents(l6)
    print_list_contents(l3)


list_tests()
