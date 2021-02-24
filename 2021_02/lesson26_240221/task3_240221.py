# task3_240221
"""
One way to improve the quicksort is to use an insertion sort on lists that are small in length
(call it the “partition limit”). Why does this make sense?
Re-implement the quicksort and use it to sort a random list of integers.
Perform analysis using different list sizes for the partition limit.
"""


def insertion_sort(array):
    insertion_sort_helper(array, 0, len(array) - 1)


def insertion_sort_helper(array, first, last):
    for index in range(first+1, last+1):
        current_value = array[index]
        position = index
        while position > first and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = current_value


def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, first, last):
    if first < last:
        split_point = partition(array, first, last)

        quick_sort_helper(array, first, split_point - 1)
        quick_sort_helper(array, split_point + 1, last)


def partition(array, first, last):
    pivot_value = array[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp

    temp = array[first]
    array[first] = array[right_mark]
    array[right_mark] = temp
    print(right_mark)

    return right_mark


# реализация быстрой сортировки с использованием сортировки вставкой для частей массива
# используя рекурсию постоянно находим размер массива
# если размер больше порогового значения 10, для этой части массива вызывается функция быстрой сортировки
# в противном случае вызывается сортировка вставкой
def hybrid_quick_sort_helper(array, first, last):
    # если размер массива меньше, чем установленный порог 10 применяем сортировку вставкой
    while first < last:
        if last - first + 1 < 10:
            insertion_sort_helper(array, first, last)
            break
        # если размер массива больше, чем установленный порог 10 применяем быструю сортировку
        else:
            pivot = partition(array, first, last)
            # если левая сторона относительно точки поворота меньше, чем правая, делаем ее гибридную сортировку
            # перемещаемся в правую часть массива
            if pivot - first < last - pivot:
                hybrid_quick_sort_helper(array, first, pivot - 1)
                first = pivot + 1
            # если правая сторона относительно точки поворота меньше, чем левая, делаем ее гибридную сортировку
            # перемещаемся в левую часть массива
            else:
                hybrid_quick_sort_helper(array, pivot + 1, last)
                last = pivot - 1


def hybrid_quick_sort(array):
    hybrid_quick_sort_helper(array, 0, len(array)-1)


if __name__ == "__main__":
    my_array = [98, 22, 4, 93, 62, 1, 57, 15, 2, 3, 34, 8, 41, 74, 12, 10]
    hybrid_quick_sort(my_array)
    print(my_array)
