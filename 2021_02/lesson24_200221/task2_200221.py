# task2_200221
"""
Implement a stack using a singly linked list.
"""
from node import Node


class Stack:
    def __init__(self):
        self._head = None

    def is_empty(self):
        if self._head is None:
            return True
        return False

    def push(self, item):
        if self._head is None:
            self._head = Node(item)
        else:
            temp = Node(item)
            temp.set_next(self._head)
            self._head = temp

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_item = self._head
            self._head = self._head.get_next
            popped_item.set_next = None
            return popped_item

    def peek(self):
        if self.is_empty():
            return None
        return self._head

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def __repr__(self):
        representation = "<Stack>\n"
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()

    s.push(4)
    s.push('dog')
    s.push(32)
    s.push(15)

    print(s)
    print(s.peek())
    print(s.size())
