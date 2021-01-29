# task3_290121
"""
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""
my_iterable = [2, 3, 5]
my_power = 4

# way_1
class MyExponentIterator:

    def __init__(self, iterable: list, power: int):
        if not isinstance(iterable, list) or not isinstance(power, int):
            raise TypeError
        self.iterable = iterable
        self.power = power
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.iterable)-1:
            raise StopIteration
        value = self.iterable[self.index] ** self.power
        self.index += 1
        return value

# way_2
def action_for_in(iterable: list, power: int):
    if not isinstance(iterable, list) or not isinstance(power, int):
        raise TypeError
    iterator = iter(iterable)
    iterating_finished = False
    while not iterating_finished:
        try:
            yield next(iterator) ** power
        except StopIteration:
            iterating_finished = True


if __name__ == "__main__":
    my_iterator1 = MyExponentIterator(my_iterable, my_power)
    for i in my_iterator1:
        print(i, end=' ')

    print(list(action_for_in(my_iterable, my_power)))
