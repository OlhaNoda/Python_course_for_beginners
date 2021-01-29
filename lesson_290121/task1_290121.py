# task1_250121
"""
Create your own implementation of a built-in function enumerate, named `with_index`,
which takes two parameters: `iterable` and `start`, default is 0.
Tips: see the documentation for the enumerate function
"""
iterable_object = 'qwerty'
start = 1

# way_1
class MyEnumerate:

    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > len(self.iterable):
            raise StopIteration
        number = self.start
        element = self.iterable[self.index]
        self.start += 1
        self.index += 1
        return number, element

# way_2
def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start+i, iterable[i]


if __name__ == "__main__":
    my_enum1 = MyEnumerate(iterable_object, start)
    for i in my_enum1:
        print(i)

    print(list(with_index(iterable_object, start)))
