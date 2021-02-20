# task2_200221
"""
Implement a stack using a singly linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'

    def __str__(self):
        return self.__repr__()


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def push(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            temp = Node(item)
            temp.next = self.head
            self.head = temp

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_item = self.head
            self.head = self.head.next
            popped_item.next = None
            return popped_item

    def peek(self):
        if self.is_empty():
            return None
        return self.head

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        representation = "<Stack>\n"
        current = self.head
        while current is not None:
            representation += f"{current.data} "
            current = current.next
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()

    s.push(4)
    s.push(72)
    s.push(32)
    s.push(15)

    print(s)
    print(s.peek())
    print(s.size())
    print(s)

    print(s.pop())
    print(s)
