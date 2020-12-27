# task4_281220
'''
Сделайте словарь дней недели {1: "Monday", 2:... } в общем словарь.
И потом "переверните" чтоб было {"Monday": 1, ...
'''
week = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
new_week = {value: key for key, value in week.items()}
print(new_week)

