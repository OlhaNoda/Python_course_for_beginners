# task2_250121
"""
Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function
"""
my_start = -4
my_end = 10
my_step = 2

# way_1
class MyRange:

    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        value = self.start
        self.start += self.step
        return value

# way_2
def in_range(start, end, step=1):
    while start < end:
        yield start
        start += step


if __name__ == "__main__":
    my_range1 = MyRange(my_start, my_end, my_step)
    for i in my_range1:
        print(i, end=' ')
    print(list(in_range(my_start, my_end, my_step)))
