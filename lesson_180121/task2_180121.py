# task2_180121
"""
Task 2
Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""


def make_sum_numbers_to_power(power):
    def sum_numbers(*numbers):
        return sum(num**power for num in numbers)
    return sum_numbers


if __name__ == "__main__":
    print(make_sum_numbers_to_power(2)(2, 3, 4))
