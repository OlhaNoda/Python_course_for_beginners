# task2_250121
"""
Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function
"""
start = -4
end = 10
step = 2


def in_range(start, end, step=1):
    while start < end:
        yield start
        start += step


if __name__ == "__main__":
    print(list(range(start, end, step)))
    print(list(in_range(start, end, step)))
