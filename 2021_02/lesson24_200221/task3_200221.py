# task3_200221
"""
Implement a queue using a singly linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def enqueue(self, item):
        if self.last is None:
            self.head = Node(item)
            self.last = self.head
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            popped_item = self.head.data
            self.head = self.head.next
            return popped_item

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        representation = "<Queue>\n"
        current = self.head
        while current is not None:
            representation += f"{current.data} "
            current = current.next
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    q = Queue()

    q.enqueue(59)
    q.enqueue(92)
    q.enqueue(2)
    q.enqueue(18)
    print(q)
    print(q.size())

    print(q.dequeue())
    print(q)
    print(q.size())

