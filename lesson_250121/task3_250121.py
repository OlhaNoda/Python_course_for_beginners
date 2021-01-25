# task3_250121
"""
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""

my_list = [5, 10, 15, 20]


def for_in(iterable):
    iterator = iter(iterable)
    completed_iterating = False
    while not completed_iterating:
        try:
            print(next(iterator))
        except StopIteration:
            completed_iterating = True


if __name__ == "__main__":
    for_in(my_list)
