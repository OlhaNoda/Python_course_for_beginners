# task1_220221
"""
Implement binary search using recursion.
"""
from typing import Union


# функция осуществтяет бинарный поиск в упорядоченном массиве и возвращает индекс искомого значения
# f((2,5,7,9,11),9) -> 3
def binary_search_recursive(array: Union[list, tuple], value: Union[int, float]) -> int:
    left = 0
    right = len(array) - 1
    middle = (left + right) // 2
    if value == array[middle]:
        return middle
    if value > array[middle]:
        return binary_search_recursive(array[middle+1:], value) + (middle+1)
    return binary_search_recursive(array[:middle], value)


if __name__ == "__main__":
    my_array = [i for i in range(100)]
    assert binary_search_recursive(my_array, 0) == 0
    assert binary_search_recursive(my_array, 99) == 99
    assert binary_search_recursive(my_array, 78) == 78
