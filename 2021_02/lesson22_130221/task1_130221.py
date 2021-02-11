# task1_130221
"""
All tasks should be solved using recursion
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
Returns  x ^ exp
ValueError: This function works only with exp > 0
"""
from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if not isinstance(x, int) and not isinstance(x, float) or not isinstance(exp, int):
        raise TypeError(f'This function {to_power.__name__} works only with x: Union[int, float], exp: int')
    if exp <= 0:
        raise ValueError(f'This function {to_power.__name__} works only with exp > 0')
    if exp == 1:
        return x
    if exp != 1:
        return x * to_power(x, exp - 1)


if __name__ == "__main__":
    assert to_power(2, 3) == 8
    assert to_power(3.5, 2) == 12.25
