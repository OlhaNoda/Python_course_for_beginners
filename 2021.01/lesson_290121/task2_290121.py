# task2_290121
"""
Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function
"""


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
"""
    def __contains__(self, item):
        return item in 
"""

if __name__ == "__main__":
    my_range = MyRange(-4, 10, 2)
    if 2 in my_range:
        print('OK')
