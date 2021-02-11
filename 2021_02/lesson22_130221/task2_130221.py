# task2_130221
"""
def is_palindrome(looking_str: str, index: int = 0) -> bool:
All tasks should be solved using recursion
"""


def is_palindrome_recursive(looking_str: str) -> bool:
    if not isinstance(looking_str, str):
        raise TypeError(f'This function {is_palindrome_recursive.__name__} works only with looking_str: str')
    if len(looking_str) < 1:
        return True
    if looking_str[0] == looking_str[-1]:
        return is_palindrome_recursive(looking_str[1:-1])
    else:
        return False


if __name__ == "__main__":
    assert is_palindrome_recursive('mom') == True
    assert is_palindrome_recursive('sassas') == True
    assert is_palindrome_recursive('0') == True
    assert is_palindrome_recursive('qwerty') == False
