"""
Дополнительная задача
Реализовать функционал, который повзоляет сдвигать цифры в числе на заданное количество шагов в любую сторону.
Вправо: последняя цифра становится первой, влево: первая цифра становится последней.
Например, для числа 1023 результатом сдвига вправо на 1 шаг будет число 3102, на 2 шага 2310 и т.д.
Результат сдвига влево, соответственно такой: 1023 -> 231 -> 2310 -> 3102 и т.д.
В коде нельзя использовать перевод числа в строку!!!
"""


# Определение количества разрядов в числе
def count_place(number: int) -> int:
    place = 1
    while number >= 10:
        number //= 10
        place *= 10
    return place


# Сдвиг цифр в числе вправо на заданное количество шагов
def shift_digits_right(number: int, step: int = 1) -> int:
    place = count_place(number)
    while step > 0:
        last_digit = number % 10  # определение последней цифры в числе
        number //= 10  # отбрасывание последней цифры из числа
        number += last_digit * place  # изменение числа - последняя цифра становится первой
        step -= 1
    return number


# Сдвиг цифр в числе влево на заданное количество шагов
def shift_digits_left(number: int, step: int = 1) -> int:
    place = count_place(number)
    while step > 0:
        first_digit = number // place  # определение первой цифры в числе
        number %= place  # отбрасывание первой цифры из числа
        number = number * 10 + first_digit  # изменение числа - первая цифра становится последней
        step -= 1
    return number


if __name__ == "__main__":
    assert shift_digits_right(1035, 3) == 351
    assert shift_digits_right(1035, 4) == 1035
    assert shift_digits_left(1035, 1) == 351
    assert shift_digits_left(1035, 2) == 3510
