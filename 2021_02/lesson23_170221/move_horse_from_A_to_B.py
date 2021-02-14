"""
Дополнительная задача.
Реализовать функционал, который определяет кратчайший путь коня на шахматной доске 8x8 из одной заданной точки в другую.
"""


def search_horse_shortest_way(x_start: int, y_start: int, x_finish: int, y_finish: int, size: int = 8) -> tuple:

    # проверяем, находится ли старт и финиш в пределах доски
    if not x_start in range(1, size+1) or not y_start in range(1, size+1) or not x_finish in range(1, size+1)\
            or not y_finish in range(1, size+1):
        raise ValueError('start and finish positions must be within the chessboard 8x8')

    # проверяем, совпадают ли старт и финиш
    pos_start = (x_start, y_start)
    pos_finish = (x_finish, y_finish)
    if pos_start == pos_finish:
        return pos_finish

    # формируем список всех возможных первых ходов коня
    ways = [(pos_start, (pos_start[0] - 1, pos_start[1] + 2)), (pos_start, (pos_start[0] + 1, pos_start[1] + 2)),
            (pos_start, (pos_start[0] + 2, pos_start[1] + 1)), (pos_start, (pos_start[0] + 2, pos_start[1] - 1)),
            (pos_start, (pos_start[0] + 1, pos_start[1] - 2)), (pos_start, (pos_start[0] - 1, pos_start[1] - 2)),
            (pos_start, (pos_start[0] - 2, pos_start[1] - 1)), (pos_start, (pos_start[0] - 2, pos_start[1] + 1))]

    # проверяем, есть ли среди первых ходов тот, который достигает цели. Отбрасываем ходы за пределами доски.
    wrong_ways = []
    for way in ways:
        if way[-1] == pos_finish:
            return way
        if not way[-1][0] in range(1, size+1) or not way[-1][-1] in range(1, size+1):
            wrong_ways.append(way)
    ways = list(set(ways) - set(wrong_ways))
    wrong_ways = []

    # для каждого из первых ходов формируем список следующих новых ходов
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
            if new_way[-1] == pos_finish:
                return new_way

            # если цель не достигнута, динамически добавляем новый ход в конец списка всех ходов
            ways.append(new_way)


if __name__ == '__main__':
    print(search_horse_shortest_way(3, 4, 3, 4))
    print(search_horse_shortest_way(1, 1, 8, 8))
    print(search_horse_shortest_way(1, 5, 1, 1))
    print(search_horse_shortest_way(1, 2, 1, 1))
