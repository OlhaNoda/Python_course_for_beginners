# task3_290121
"""
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""

# way_1
class MyIterator:

    def __init__(self, *args):
        self.iterable = args
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.iterable)-1:
            raise StopIteration
        value = self.iterable[self.index]
        self.index += 1
        return value

# way_2
def my_generator(*args):
    iterator = iter(args)
    iterating_finished = False
    while not iterating_finished:
        try:
            yield next(iterator)
        except StopIteration:
            iterating_finished = True


if __name__ == "__main__":
    my_iterator = MyIterator(1, 2, 3, '432', 433, {1, 2, 3})
    for i in my_iterator:
        print(i)
    for i in my_generator(1, 2, 3, '432', 433, {1, 2, 3}):
        print(i)

