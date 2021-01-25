# task3_250121
"""
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""

my_list = [5, 10, 15, 20]


def my_for_in(iterable):
    iterator = iter(iterable)
    iterating_finished = False
    while not iterating_finished:
        try:
            print(next(iterator))
        except StopIteration:
            iterating_finished = True


if __name__ == "__main__":
    my_for_in(my_list)
