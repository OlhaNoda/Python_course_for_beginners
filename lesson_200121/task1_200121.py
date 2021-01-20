# task1_200121
"""
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
"add called with 4, 5"
"""
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args):
        print(f'{func.__name__} called with {args}')
        return func(*args)
    return wrapper


@logger
def add(*args):
    return sum(arg for arg in args)


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == "__main__":
    add(1, 2)
    square_all(3, 4, 5)
