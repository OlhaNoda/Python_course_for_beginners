# task1_240221
"""
A bubble sort can be modified to “bubble” in both directions.
The first pass moves “up” the list and the second pass moves “down.”
This alternating pattern continues until no more passes are necessary.
Implement this variation and describe under what circumstances it might be appropriate.
"""


def bidirectional_bubble_sort(array):
    start = 0
    end = len(array) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start += 1


if __name__ == "__main__":
    my_array = [98, 22, 4, 93, 62, 1, 57, 15, 2, 3]
    bidirectional_bubble_sort(my_array)
    print(my_array)
