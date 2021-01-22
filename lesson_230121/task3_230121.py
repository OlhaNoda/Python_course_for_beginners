# task3_230121
"""
Write a class TypeDecorators which has several methods for converting results of functions
to a specified type (if it's possible):
methods:
to_int
to_str
to_bool
to_float
Don't forget to use @wraps
"""
from functools import wraps


class TypeDecorators:

    @classmethod
    def to_int(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return int(func(*args, **kwargs))
            except ValueError:
                return False, 'error'
        return wrapper

    @classmethod
    def to_str(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return str(func(*args, **kwargs))
        return wrapper

    @classmethod
    def to_bool(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return bool(func(*args, **kwargs))
        return wrapper

    @classmethod
    def to_float(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return float(func(*args, **kwargs))
            except ValueError:
                return False, 'error'
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


if __name__ == "__main__":
    assert do_nothing('25') == 25
    assert do_something('True') is True
