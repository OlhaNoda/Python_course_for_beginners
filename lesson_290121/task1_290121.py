# task1_250121
"""
Create your own implementation of a built-in function enumerate, named `with_index`,
which takes two parameters: `iterable` and `start`, default is 0.
Tips: see the documentation for the enumerate function
"""
iterable_object = 'qwerty'
start = 1


def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start+i, iterable[i]


if __name__ == "__main__":
    print(enumerate(iterable_object, start))
    print(list(enumerate(iterable_object, start)))
    print(with_index(iterable_object, start))
    print(list(with_index(iterable_object, start)))
