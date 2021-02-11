# task5_130221
"""
def sum_of_digits(digit_string: str) -> int:
input string must be digit string
All tasks should be solved using recursion
"""


def sum_of_digits_recursive(digit_string: str) -> int:
    if not isinstance(digit_string, str):
        raise TypeError(f'This function {sum_of_digits_recursive.__name__} works only with digit_string: str')
    if digit_string != '':
        if not digit_string.isdigit():
            raise TypeError(f'This function {sum_of_digits_recursive.__name__} works only with digit string')
    if digit_string == '':
        return 0
    return int(digit_string[0]) + sum_of_digits_recursive(digit_string.replace(digit_string[0], ''))


if __name__ == "__main__":
    assert sum_of_digits_recursive('26') == 8
