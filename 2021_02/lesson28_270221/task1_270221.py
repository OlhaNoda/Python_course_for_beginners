# task1_270221
"""
Implement a binary heap as a max heap.
"""


class MaxBinHeap:

    def __init__(self) -> None:
        self.heap_list: list[int] = [0]
        self.current_size: int = 0

    def max_child(self, i) -> int:
        if i * 2 + 1 > self.current_size:
            return i * 2
        if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def perc_up(self, i) -> None:
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i //= 2

    def perc_down(self, i) -> None:
        while (i * 2) <= self.current_size:
            mc = self.max_child(i)
            if self.heap_list[i] < self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def build_heap(self, items: list[int]) -> None:
        i = len(items) // 2
        self.current_size = len(items)
        self.heap_list = [0] + items[:]
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


if __name__ == "__main__":
    my_heap = MaxBinHeap()
    my_heap.build_heap([4, 7, 1, 2, 9, 12, 5])
    print(my_heap.heap_list)
    my_heap.insert(20)
    print(my_heap.heap_list)
    my_heap.del_max()
    print(my_heap.heap_list)
