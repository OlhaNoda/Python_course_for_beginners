# task2_270221
"""
Using the BinaryHeap class, implement a new class called PriorityQueue.
Your PriorityQueue class should implement the constructor, plus the enqueue and dequeue methods.
"""


class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __repr__(self):
        return f'{self.data} - {self.priority}'


class MaxBinHeap:
    def __init__(self) -> None:
        self.heap_list: list = [0]
        self.current_size: int = 0

    def max_child(self, i) -> int:
        if i * 2 + 1 > self.current_size:
            return i * 2
        if self.heap_list[i * 2].priority > self.heap_list[i * 2 + 1].priority:
            return i * 2
        else:
            return i * 2 + 1

    def perc_up(self, i) -> None:
        while i // 2 > 0:
            if self.heap_list[i].priority > self.heap_list[i // 2].priority:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i //= 2

    def perc_down(self, i) -> None:
        while (i * 2) <= self.current_size:
            mc = self.max_child(i)
            if self.heap_list[i].priority < self.heap_list[mc].priority:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def build_heap(self, items: list) -> None:
        i = len(items) // 2
        self.current_size = len(items)
        self.heap_list = [0, 0] + items[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

    def insert(self, k) -> None:
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def del_max(self) -> int:
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val


class PriorityQueue:
    def __init__(self):
        self.queue = MaxBinHeap()

    def enqueue(self, node):
        self.queue.insert(node)

    def dequeue(self):
        self.queue.del_max()

    def __repr__(self):
        return f'{self.queue.heap_list}'


if __name__ == "__main__":
    x1 = Node('a', 2)
    x2 = Node('b', 7)
    x3 = Node('c', 1)
    x4 = Node('d', 4)
    x5 = Node('e', 8)
    x6 = Node('f', 5)
    x7 = Node('g', 9)
    pq = PriorityQueue()
    pq.enqueue(x1)
    pq.enqueue(x2)
    pq.enqueue(x3)
    pq.enqueue(x4)
    pq.enqueue(x5)
    pq.enqueue(x6)
    pq.enqueue(x7)
    print(pq)
    pq.dequeue()
    print(pq)
