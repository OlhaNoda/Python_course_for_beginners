
def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start+i, iterable[i]


def in_range(start, end, step=1):
    while start < end:
        yield start
        start += step


def my_generator(*args):
    iterator = iter(args)
    iterating_finished = False
    while not iterating_finished:
        try:
            yield next(iterator)
        except StopIteration:
            iterating_finished = True


if __name__ == "__main__":
    print(list(with_index('qwerty', 1)))
    if 2 in in_range(-4, 10, 2):
        print('OK')
    for i in my_generator(1, 2, 3, '432', 433, {1, 2, 3}):
        print(i)

