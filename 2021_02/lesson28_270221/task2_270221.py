# task2_270221
"""
Using the BinaryHeap class, implement a new class called PriorityQueue.
Your PriorityQueue class should implement the constructor, plus the enqueue and dequeue methods.
"""

from task1_270221 import MaxBinHeap


class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __repr__(self):
        return f'{self.data} - {self.priority}'


class PriorityQueue:
    def __init__(self):
        self.queue = MaxBinHeap()

    def enqueue(self, node):
        self.queue.insert(node.priority)

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



