# task3_250121
"""
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""

my_list = [5, 10, 15, 20]


def action_for_in(iterable, action):
    iterator = iter(iterable)
    iterating_finished = False
    while not iterating_finished:
        try:
            yield action(next(iterator))
        except StopIteration:
            iterating_finished = True


def power_to_2(number):
    return number ** 2


if __name__ == "__main__":
    print(list(action_for_in(my_list, power_to_2)))
