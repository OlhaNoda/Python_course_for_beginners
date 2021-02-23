# task2_240221
"""
Implement the mergeSort function without using the slice operator.
"""


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = []
        right_half = []
        for index in range(mid):
            left_half.append(array[index])
        for index in range(mid, len(array)):
            right_half.append(array[index])

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1


if __name__ == "__main__":
    my_array = [98, 22, 4, 93, 62, 1, 57, 15, 2, 3]
    merge_sort(my_array)
    print(my_array)
