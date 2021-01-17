# task2_180121
"""
Task 2
Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""

from functools import reduce


def make_sum_numbers_to_power_function(power):
    def sum_numbers(*numbers):
        return reduce(lambda x, y: x+y**power, numbers)
    return sum_numbers


if __name__ == "__main__":
    sum_numbers_to_power_2 = make_sum_numbers_to_power_function(2)
    print(sum_numbers_to_power_2(1, 2, 3))
