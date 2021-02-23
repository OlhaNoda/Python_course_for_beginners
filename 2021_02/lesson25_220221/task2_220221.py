# task2_220221
"""
Read about the Fibonacci search and implement it using python.
Explore its complexity and compare it to sequential, binary searches.
"""


def fibonacci_search(lys, val):
    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = fib_minus_1 + fib_minus_2
    while fib < len(lys):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2
    index = -1
    while fib > 1:
        i = min(index + fib_minus_2, (len(lys)-1))
        if lys[i] < val:
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            index = i
        elif lys[i] > val:
            fib = fib_minus_2
            fib_minus_1 = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib - fib_minus_1
        else:
            return i
    if fib_minus_1 and index < (len(lys) - 1) and lys[index + 1] == val:
        return index+1
    return -1


if __name__ == "__main__":
    my_array = [i for i in range(100)]
    assert fibonacci_search(my_array, 0) == 0
    assert fibonacci_search(my_array, 99) == 99
    assert fibonacci_search(my_array, 78) == 78
    print(fibonacci_search(my_array, 200))
