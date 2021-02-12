# task4_130221
"""
def reverse(input_str: str) -> str:
Function returns reversed input string
All tasks should be solved using recursion
"""


def reverse_recursive(input_str: str) -> str:
    if not isinstance(input_str, str):
        raise TypeError(f'The function {reverse_recursive.__name__} works only with input_str: str')
    if len(input_str) == 0:
        return input_str
    return reverse_recursive(input_str[1:])+input_str[0]


if __name__ == "__main__":
    assert reverse_recursive('hello') == 'olleh'
    assert reverse_recursive('o') == 'o'
