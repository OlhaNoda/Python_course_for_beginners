"""
Дополнительная задача
Реализовать функционал, который позволяет сдвигать цифры в числе на заданное количество шагов в какую-либо сторону.
Вправо: последняя цифра становится первой, влево: первая цифра становится последней.
Например, для числа 1023 результатом сдвига вправо на 1 шаг будет число 3102, на 2 шага 2310 и т.д.
Результат сдвига влево, соответственно такой: 1023 -> 231 -> 2310 -> 3102 и т.д.
В коде нельзя использовать перевод числа в строку!
"""


# Определение количества разрядов в числе
# f(2) -> 1, f(23) -> 2, f(231) -> 3, f(2310) -> 4 и т.д.
def count_places(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError(f'The function {count_places.__name__} works only with number: int')
    if number < 0:
        raise ValueError(f'The function {count_places.__name__} works only with number > 0')
    places = 0
    while number >= 1:
        number //= 10
        places += 1
    return places


# Сдвиг цифр в числе вправо на заданное количество шагов
def shift_digits_right(number: int, step: int = 1) -> int:
    if not isinstance(number, int) or not isinstance(step, int):
        raise TypeError(f'The function {shift_digits_right.__name__} works only with number: int, step: int')
    if step < 0:
        raise ValueError(f'The function {shift_digits_right.__name__} works only with step >= 0')
    places = count_places(number)
    while step > 0:
        last_digit = number % 10  # определение последней цифры в числе
        number //= 10  # отбрасывание последней цифры из числа
        number += last_digit * 10**(places-1)  # изменение числа - последняя цифра становится первой
        step -= 1
    return number


# Сдвиг цифр в числе влево на заданное количество шагов
def shift_digits_left(number: int, step: int = 1) -> int:
    if not isinstance(number, int) or not isinstance(step, int):
        raise TypeError(f'The function {shift_digits_left.__name__} works only with number: int, step: int')
    if step < 0:
        raise ValueError(f'The function {shift_digits_left.__name__} works only with step >= 0')
    places = count_places(number)
    while step > 0:
        first_digit = number // 10**(places-1)  # определение первой цифры в числе
        number %= 10**(places-1)  # отбрасывание первой цифры из числа
        number = number * 10 + first_digit  # изменение числа - первая цифра становится последней
        step -= 1
    return number


if __name__ == "__main__":
    assert shift_digits_right(1035, 3) == 351
    assert shift_digits_right(1035, 4) == 1035
    assert shift_digits_left(1035, 1) == 351
    assert shift_digits_left(1035, 2) == 3510
