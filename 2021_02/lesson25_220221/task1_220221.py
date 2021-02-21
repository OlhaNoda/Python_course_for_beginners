# task1_220221
"""
Implement binary search using recursion.
"""


def binary_search_recursive(array, item):
    first = 0
    last = len(array) - 1
    midpoint = (first + last) // 2
    if item == array[midpoint]:
        return midpoint
    if item > array[midpoint]:
        return binary_search_recursive(array[midpoint+1:], item) + (midpoint + 1)
    return binary_search_recursive(array[:midpoint], item)


if __name__ == "__main__":
    my_array = [i for i in range(100)]
    assert binary_search_recursive(my_array, 0) == 0
    assert binary_search_recursive(my_array, 99) == 99
    assert binary_search_recursive(my_array, 78) == 78
