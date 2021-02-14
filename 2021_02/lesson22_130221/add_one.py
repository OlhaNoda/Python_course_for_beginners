"""
Дополнительная задача.
Реализовать функцию, которая принимает список целых чисел, и добавляет к последнему в спике числу единицу.
При этом если последнее число 9, то после прибавления единицы, оно становится нулем.
А единица добавляется к предыдущему числу в списке.
f(123) -> 124
f(129) -> 130
f(199) -> 200
f(999) -> 1000
"""


def add_one(my_list, pos=0):
    index = len(my_list)-1-pos
    if index < 0:
        return [1] + my_list
    my_list[index] += 1
    if my_list[index] < 10:
        return my_list
    if my_list[index] == 10:
        my_list[index] = 0
        return add_one(my_list, pos + 1)


if __name__ == "__main__":
    print(add_one([1, 2, 3]))
    print(add_one([9, 9, 9]))
    print(add_one([1, 2, 9, 9]))
    print(add_one([1, 0, 9]))
