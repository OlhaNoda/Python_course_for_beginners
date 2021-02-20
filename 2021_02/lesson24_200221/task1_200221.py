# task1_200221
"""
Extend UnorderedList
Implement append, index, pop, insert methods for UnorderedList.
Also implement a slice method, which will take two parameters `start` and `stop`,
and return a copy of the list starting at the position and going up to but not including the stop position.
"""

from node import Node


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        current = self._head
        temp = Node(item)
        temp.set_next(None)
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(temp)

    def index(self, item):
        current = self._head
        found = False
        index = 0
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                index += 1
        if not found:
            index = None
        return index

    def pop(self, index=None):
        if self.is_empty():
            return None
        if index is None:
            index = self.size()-1
        current = self._head
        previous = None
        for i in range(index):
            previous = current
            current = current.get_next()
        popped_item = current
        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return popped_item

    def insert(self, index, item):
        temp = Node(item)
        if index == 0:
            temp.set_next(self._head)
            self._head = temp
        else:
            if index > self.size():
                index = self.size()
            current = self._head
            for i in range(index-1):
                current = current.get_next()
            temp.set_next(current.get_next())
            current.set_next(temp)

    def slice(self, start, stop):
        if start > stop:
            raise ValueError
        else:
            slice_list = UnorderedList()
            current = self._head
            for i in range(start):
                current = current.get_next()
            for i in range(start, stop):
                slice_list.add(current)
                current = current.get_next()
        return slice_list

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(95)
    my_list.add(54)

    print(my_list)

    my_list.append(14)

    print(my_list)

    print(my_list.index(77))

    print(my_list.pop())
    print(my_list)

    print(my_list.pop(1))
    print(my_list)

    my_list.insert(5, 15)
    print(my_list)

    print(my_list.slice(1, 3))
