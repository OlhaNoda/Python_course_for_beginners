# task3_130221
"""
def mult(a: int, n: int) -> int:
This function works only with positive integers
All tasks should be solved using recursion
"""


def mult_recursive(a: int, n: int) -> int:
    if not isinstance(a, int) or not isinstance(n, int):
        raise TypeError(f'This function {mult_recursive.__name__} works only with a: int, n: int')
    if n < 0:
        raise ValueError(f'This function {mult_recursive.__name__} works only with n >= 0')
    if n == 0:
        return 0
    return a + mult_recursive(a, n-1)


if __name__ == "__main__":
    assert mult_recursive(2, 4) == 8
    assert mult_recursive(2, 0) == 0
