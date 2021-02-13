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


# Сдвиг цифр в числе вправо на заданное количество шагов
def shift_digits_right_recursive(number: int, step: int, flag=0) -> int:
    if not isinstance(number, int) or not isinstance(step, int):
        raise TypeError(f'The function {shift_digits_right_recursive.__name__} works only with number: int, step: int')
    if step < 0:
        raise ValueError(f'The function {shift_digits_right_recursive.__name__} works only with step >= 0')
    if flag != 0 and flag != 1:
        raise ValueError(f'The function {shift_digits_right_recursive.__name__} works only with flag = 0 or flag = 1')
    places = count_places_recursive(number) + flag
    flag = 0
    if step == 0:
        return number
    last_digit = number % 10  # определение последней цифры в числе
    if last_digit == 0:
        flag = 1
    number //= 10  # отбрасывание последней цифры из числа
    number += last_digit * 10**(places-1)  # изменение числа - последняя цифра становится первой
    return shift_digits_right_recursive(number, step - 1, flag)


def delete_contact_by_phone(file_name, phone):
    load_file = read_file(file_name)
    for entry in load_file:
        if entry['phone'] == phone:
            load_file.remove(entry)
    rewrite_file(file_name, load_file)

import math


def make_volume_threedimensional_shape(shape: str):
    def volume_shape(r=0.0, h=0.0):
        formula_dict = {
            'шар': 4 / 3 * math.pi * r ** 3,
            'конус': 1 / 3 * math.pi * r ** 2 * h,
            'цилиндр': math.pi * r ** 2 * h
        }
        return [formula_dict[key] for key in formula_dict if key == shape]
    return volume_shape


if __name__ == "__main__":
    print(make_volume_threedimensional_shape('конус')(1.52, 2))


# way_2
def action_for_in(iterable: list):
    if not isinstance(iterable, list):
        raise TypeError
    iterator = iter(iterable)
    iterating_finished = False
    while not iterating_finished:
        try:
            yield next(iterator)
        except StopIteration:
            iterating_finished = True
