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
def count_places_recursive(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError(f'The function {count_places_recursive.__name__} works only with number: int')
    if number < 0:
        raise ValueError(f'The function {count_places_recursive.__name__} works only with number > 0')
    if number == 0:
        return 0
    return 1 + count_places_recursive(number // 10)


def shift_digits_left_recursive(number: int, step: int = 1) -> int:
    if not isinstance(number, int) or not isinstance(step, int):
        raise TypeError(f'The function {shift_digits_left_recursive.__name__} works only with number: int, step: int')
    if step < 0:
        raise ValueError(f'The function {shift_digits_left_recursive.__name__} works only with step >= 0')
    places = count_places_recursive(number)
    if step == 0:
        return number
    first_two_digits = number // 10**(places-2)  # определение первых двух цифр в числе
    if first_two_digits % 10 == 0 and step != 1:  # если число из первых двух цифр кратно 10 и это не последний шаг
        number %= 10**(places-2)  # отбрасывание первых двух цифр из числа
        number = number*100 + first_two_digits  # изменение числа - первые две цифры становятся последними
        return shift_digits_left_recursive(number, step - 2)
    else:
        first_digit = number // 10**(places-1)  # определение первой цифры в числе
        number %= 10**(places-1)  # отбрасывание первой цифры из числа
        number = number * 10 + first_digit  # изменение числа - первая цифра становится последней
        return shift_digits_left_recursive(number, step - 1)


if __name__ == "__main__":
    print(shift_digits_left_recursive(10, 2))

