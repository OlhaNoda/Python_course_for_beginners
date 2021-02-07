from typing import Any, Iterator, Sequence


def my_enumerate(iterable: Sequence[Any], start: int = 0) -> Iterator[tuple[int, Any]]:
    for i in range(len(iterable)):
        yield start+i, iterable[i]


def my_range(start: int, end: int, step: int = 1) -> Iterator[int]:
    while start < end:
        yield start
        start += step


def my_generator(*args: Any) -> Iterator[Any]:
    iterator = iter(args)
    iterating_finished = False
    while not iterating_finished:
        try:
            yield next(iterator)
        except StopIteration:
            iterating_finished = True
