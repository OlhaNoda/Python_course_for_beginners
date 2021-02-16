"""
Дополнительная задача.
Реализовать функционал, который определяет кратчайший путь коня на шахматной доске 8x8 из одной заданной точки в другую.
"""


# функция преобразует результат функции search_horse_shortest_way
# выпрямляет кортеж, убирает из него нулевой ход
def pars_way(way: tuple) -> tuple:
    if isinstance(way[0], tuple):
        return pars_way(way[0])+way[1:]
    return ()


# функция возвращает первый найденный кратчайший путь шахматного коня из точки А в точку В на доске с заданным размером
def search_horse_shortest_way(x_start: int, y_start: int, x_finish: int, y_finish: int, size: int = 8) -> tuple:

    # проверяем, находится ли старт и финиш в пределах доски
    if not x_start in range(1, size+1) or not y_start in range(1, size+1) or not x_finish in range(1, size+1)\
            or not y_finish in range(1, size+1):
        raise ValueError(f'start and finish positions must be within the chessboard {size}x{size}')

    # проверяем, совпадают ли старт и финиш
    if x_start == x_finish and y_start == y_finish:
        return ()

    # формируем список всех ходов WAYS с нулевым ходом
    ways = [((x_start, y_start), (x_start, y_start))]

    # для каждого хода из списка всех ходов WAYS формируем список следующих новых ходов
    wrong_ways = []
    for way in ways:
        new_ways = [(way, (way[-1][0] - 1, way[-1][-1] + 2)), (way, (way[-1][0] + 1, way[-1][-1] + 2)),
                    (way, (way[-1][0] + 2, way[-1][-1] + 1)), (way, (way[-1][0] + 2, way[-1][-1] - 1)),
                    (way, (way[-1][0] + 1, way[-1][-1] - 2)), (way, (way[-1][0] - 1, way[-1][-1] - 2)),
                    (way, (way[-1][0] - 2, way[-1][-1] - 1)), (way, (way[-1][0] - 2, way[-1][-1] + 1))]

        # отбрасываем новые ходы за пределами доски
        for new_way in new_ways:
            if not new_way[-1][0] in range(1, size+1) or not new_way[-1][-1] in range(1, size+1):
                wrong_ways.append(new_way)
        new_ways = list(set(new_ways) - set(wrong_ways))
        wrong_ways = []

        # проверяем есть ли среди новых ходов тот, который достигает цели
        for new_way in new_ways:
            if new_way[-1] == (x_finish, y_finish):
                return pars_way(new_way)

            # если цель не достигнута добавляем новый ход в конец списка всех ходов WAYS
            ways.append(new_way)


if __name__ == '__main__':
    print(search_horse_shortest_way(3, 4, 3, 4))
    print(search_horse_shortest_way(1, 1, 8, 8))
    print(search_horse_shortest_way(1, 5, 1, 1))
    print(search_horse_shortest_way(1, 2, 1, 1))
