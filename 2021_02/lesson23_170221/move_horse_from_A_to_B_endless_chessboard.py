"""
Дополнительная задача.
Реализовать функционал, который определяет кратчайший путь коня на шахматной доске из одной заданной точки в другую.
"""


def search_horse_shortest_way(x_start, y_start, x_finish, y_finish):
    pos_start = (x_start, y_start)
    pos_finish = (x_finish, y_finish)
    if pos_start == pos_finish:
        return pos_start, pos_finish
    # формируем список всех возможных первых ходов коня
    ways = [(pos_start, (pos_start[0] - 1, pos_start[1] + 2)), (pos_start, (pos_start[0] + 1, pos_start[1] + 2)),
            (pos_start, (pos_start[0] + 2, pos_start[1] + 1)), (pos_start, (pos_start[0] + 2, pos_start[1] - 1)),
            (pos_start, (pos_start[0] + 1, pos_start[1] - 2)), (pos_start, (pos_start[0] - 1, pos_start[1] - 2)),
            (pos_start, (pos_start[0] - 2, pos_start[1] - 1)), (pos_start, (pos_start[0] - 2, pos_start[1] + 1))]
    # проверяем есть ли среди первых ходов тот, который достигает цели
    for way in ways:
        if way[-1] == pos_finish:
            return way
    # для каждого из первых ходов формируем кортеж новых ходов
    for way in ways:
        new_ways = ((way, (way[-1][0] - 1, way[-1][-1] + 2)), (way, (way[-1][0] + 1, way[-1][-1] + 2)),
                    (way, (way[-1][0] + 2, way[-1][-1] + 1)), (way, (way[-1][0] + 2, way[-1][-1] - 1)),
                    (way, (way[-1][0] + 1, way[-1][-1] - 2)), (way, (way[-1][0] - 1, way[-1][-1] - 2)),
                    (way, (way[-1][0] - 2, way[-1][-1] - 1)), (way, (way[-1][0] - 2, way[-1][-1] + 1)))
        # проверяем есть ли среди новых ходов тот, который достигает цели
        for new_way in new_ways:
            if new_way[-1] == pos_finish:
                return new_way
            # если цель не достигнута, добавляем в список всех ходов, кортеж новых ходов
            ways.append(new_way)


if __name__ == '__main__':
    print(search_horse_shortest_way(4, 5, 8, 8))
    print(search_horse_shortest_way(1, 2, 8, 8))
    print(search_horse_shortest_way(4, 5, 5, 7))
