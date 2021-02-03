# task3_290121
"""
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""


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

    def __getitem__(self, item):
        return self.iterable[item]


if __name__ == "__main__":
    my_iterator = MyIterator(1, 2, 3, '432', 433, {1, 2, 3})
    for i in my_iterator:
        print(i)
    print(my_iterator[3])
