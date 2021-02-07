from typing import Any, Sequence

my_iterable = 'qwerty'
my_start = 1


class MyEnumerate:

    def __init__(self, iterable: Sequence, start: int = 0) -> None:
        self.iterable = iterable
        self.start = start
        self._index: int = 0

    def __iter__(self) -> 'MyEnumerate':
        return self

    def __next__(self) -> tuple[int, Any]:
        if self.start > len(self.iterable):
            raise StopIteration
        number = self.start
        element = self.iterable[self._index]
        self.start += 1
        self._index += 1
        return number, element
