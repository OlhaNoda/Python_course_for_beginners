# task1_180121
"""
Task 1
Write a Python program to detect the number of local variables declared in a function.
"""


def my_func():
    a, b = 1, 2
    my_list = [7, 3, 1]
    sum_list = [i for i in my_list]
    my_str = 'qwerty'
    my_dict = {}


print(f'The number of local variables declared in a function {my_func.__name__}: {my_func.__code__.co_nlocals}')
